from annoying.functions import get_object_or_None
import musictherapy.models as models
import uuid

from collections import defaultdict
import pygal


class SkillsData(object):
    def __init__(self, domain, user):
        self.user = user
        self.domain = domain
        self.domain_model = None
        self.all_domains = None
        self.sub_domains = None
        self.all_measurables = None

    def measurables(self):
        if self.all_measurables:
            return self.all_measurables

        self.domain_model = get_object_or_None(models.Domains, name=self.domain)
        domains = [self.domain_model]
        if self.domain_model:
            domains += models.Domains.objects.filter(parent=self.domain_model, enabled=1)

        self.all_domains = domains

        measurables = defaultdict(list)
        for measurable in models.DomainMeasurables.objects.filter(domain__in=domains, enabled=1):
            measurables[measurable.domain.name] += [measurable]

        self.all_measurables = dict(measurables)

        return self.all_measurables

    def has_goal(self):
        if not self.all_domains:
            self.measurables()

        goals = models.Goals.objects.filter(domain__in=self.all_domains, enabled=1)
        return models.UserGoals.objects.filter(goal__in=goals).count() > 0

    def goals_measurables(self):
        if not self.all_domains:
            self.measurables()

        goals = models.Goals.objects.filter(domain__in=self.all_domains, enabled=1)
        user_goals = models.UserGoals.objects.filter(goal__in=goals)
        goals_measurables = models.GoalsMeasurables.objects.filter(goal__in=[ug.goal for ug in user_goals], enabled=1)
        return goals_measurables

    def past_measurables(self):
        users_measurables = models.UserMeasurables.objects.filter(user=self.user)

        past_measurables = defaultdict(list)
        for um in users_measurables:
            if um.measurable.domain in self.all_domains:
                past_measurables[um.updated] += [um]

        data = dict(fields=[], data=[])
        for date, data_list in past_measurables.iteritems():
            sub_domain_value = defaultdict(list)
            for um in data_list:
                if um.value*um.measurable.pos_neg == -1:
                    sub_domain_value[um.measurable.domain.name] += ['--']
                else:
                    sub_domain_value[um.measurable.domain.name] += [um.value]

            for domain in sub_domain_value.keys():
                cleaned_data = [float(v)/4 for v in sub_domain_value[domain] if v != '--']
                sub_domain_value[domain] = sum(cleaned_data)*100 / len(cleaned_data) if len(cleaned_data) > 0 else '--'
            sub_domain_value['Updated'] = date
            data['data'].append(dict(sub_domain_value))

        if len(data['data']) > 0:
            data['fields'] = [k for k in data['data'][0].keys() if k != 'Updated'] + ['Updated']
            data['data'] = sorted(data['data'], key=lambda field: field['Updated'], reverse=True)
            return data
        else:
            return None

    def summary_measurable(self):
        past_measurables = self.past_measurables()
        if past_measurables:
            data = []
            for measurables in past_measurables['data']:
                values = [value for key, value in measurables.iteritems() if key != 'Updated' and value != '--']
                measurables['Total'] = sum(values)/len(values) if len(values) > 0 else '--'
                measurables['id'] = str(uuid.uuid4())
                data.append(measurables)
            return {
                'fields': past_measurables['fields'] + ['Total'],
                'data': sorted(data, key=lambda measurable: measurable['Updated'], reverse=True),
            }
        else:
            return None

    def chart(self):
        if self.has_goal():
            line_chart = pygal.Line(truncate_legend=30)
            goals = self.goals_measurables()
            data = dict()
            for goal in goals:
                updates = models.UserGoalMeasurables.objects.filter(goal_measurable=goal).order_by('-updated')
                data[goal.name] = {update.updated: update.value if update.value != -1 else None for update in updates}

            all_dates = set()
            for updates in data.itervalues():
                for date in updates.iterkeys():
                    all_dates.add(date)
            all_dates = sorted(all_dates)

            for goal in data.iterkeys():
                updates = [data[goal][date] if date in data[goal] else None for date in all_dates]
                line_chart.add(goal, updates)

            line_chart.x_labels = map(str, all_dates)
            return line_chart.render(is_unicode=True, disable_xml_declaration=True)
        else:
            return None

    def to_dict(self):
        return dict(
            measurables=self.measurables(),
            has_goals=self.has_goal(),
            past_measurables=self.past_measurables(),
            goals_measurables=self.goals_measurables(),
            chart=self.chart()
        )


# both should be a UserMeasurable
def measurable_comparison(x, y):
    if x.measurable.domain > y.measurable.domain:
        return 1
    elif x.measurable.domain == y.measurable.domain:
        if x.measurable.name > y.measurable.name:
            return 1
        else:
            return -1
    else:
        return -1
