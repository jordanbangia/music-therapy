import uuid
from collections import defaultdict

import pygal
from annoying.functions import get_object_or_None

import musictherapy.models as models
from musictherapy.sessions import get_current_session, get_latest_session, get_all_sessions


class SkillsData(object):
    def __init__(self, domain, user):
        self.user = user
        self.domain = domain
        self.domain_model = None
        self.all_domains = None
        self.sub_domains = None
        self.all_measurables = None
        self.goals = None

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
        if not self.goals:
            if not self.all_domains:
                self.measurables()
            self.goals = models.Goals.objects.filter(domain__in=self.all_domains, enabled=1)
        return models.UserGoals.objects.filter(goal__in=self.goals).count() > 0

    def goals_measurables(self, session):
        if not self.all_domains:
            self.measurables()

        goals = models.Goals.objects.filter(domain__in=self.all_domains, enabled=1)
        user_goals = models.UserGoals.objects.filter(goal__in=goals, session=session)
        goals_measurables = models.GoalsMeasurables.objects.filter(goal__in=[ug.goal for ug in user_goals], enabled=1)
        return goals_measurables

    def custom_goals(self, session):
        if not self.all_domains:
            self.measurables()

        goals = models.Goals.objects.filter(domain__in=self.all_domains, enabled=1, is_custom=1, user=self.user)
        user_goals = models.UserGoals.objects.filter(goal__in=goals, session=session)
        return [ug.goal for ug in user_goals]

    def all_user_measurables(self):
        if not self.all_domains:
            self.measurables()

        user_measurables = models.UserMeasurables.objects.filter(user=self.user)
        notes = models.UserDomainNoteMeasurables.objects.filter(user=self.user, domain=self.domain_model)

        past_measurables = defaultdict(list)
        for um in user_measurables:
            if um.measurable.domain in self.all_domains:
                past_measurables[um.updated] += [um]

        for note in notes:
            past_measurables[note.updated] += [note]

        return dict(past_measurables)

    def latest_user_measurables(self):
        measurables = self.all_user_measurables()

        dates = sorted(measurables.keys(), reverse=True)
        return measurables[dates[0]] if len(dates) > 0 else None

    def past_measurables(self):
        if not self.all_domains:
            self.measurables()

        past_measurables = self.all_user_measurables()

        data = dict(fields=[], data=[])
        for date, data_list in past_measurables.iteritems():
            sub_domain_value = defaultdict(list)
            for um in data_list:
                if isinstance(um, models.UserDomainNoteMeasurables):
                    sub_domain_value['Note'] = um.note
                elif um.value == -1:
                    sub_domain_value[um.measurable.domain.name] += ['--']
                else:
                    sub_domain_value[um.measurable.domain.name] += [um.value*um.measurable.pos_neg]

            for domain in sub_domain_value.keys():
                if domain == 'Note':
                    continue
                cleaned_data = [float(v)/3 for v in sub_domain_value[domain] if v != '--']
                sub_domain_value[domain] = sum(cleaned_data)*100 / len(cleaned_data) if len(cleaned_data) > 0 else '--'
            sub_domain_value['Updated'] = date
            sub_domain_value['id'] = str(uuid.uuid4())
            data['data'].append(dict(sub_domain_value))

        if len(data['data']) > 0:
            data['fields'] = [k for k in data['data'][0].keys() if k.lower() not in ['updated', 'note', 'id']] + ['Updated', 'Note']
            data['data'] = sorted(data['data'], key=lambda field: field['Updated'], reverse=True)
            return data
        else:
            return None

    def summary_measurable(self):
        past_measurables = self.past_measurables()
        if past_measurables:
            data = []
            for measurables in past_measurables['data']:
                values = [value for key, value in measurables.iteritems() if key not in ['Updated', 'Note', 'id'] and value != '--']
                measurables['Total'] = sum(values)/len(values) if len(values) > 0 else '--'
                data.append(measurables)
            return {
                'fields': past_measurables['fields'] + ['Total'],
                'data': sorted(data, key=lambda measurable: measurable['Updated'], reverse=True),
            }
        else:
            return None

    def latest_summary_measurable(self):
        past_measruables = self.summary_measurable()
        if past_measruables:
            past_measruables['data'] = past_measruables['data'][:1]
        return past_measruables

    def latest_goals_measurables(self, return_model=False):
        goals = self.goals_measurables(get_latest_session(self.user))
        data = dict()

        for goal in goals:
            updates = models.UserGoalMeasurables.objects.filter(goal_measurable=goal)
            updates = sorted(updates, key=lambda u: u.session.date, reverse=True)
            if return_model:
                data[goal.name] = [update for update in updates if update.session]
            else:
                data[goal.name] = [update.value if update.value != -1 else None for update in updates if update.session]
            if len(data[goal.name]) > 0:
                data[goal.name] = data[goal.name][0]

        notes = models.UserGoalNoteMeasurable.objects.filter(session=get_latest_session(self.user), domain=self.domain_model)
        return {'data': data, 'notes': notes,} if len(data) > 0 or len(notes) > 0 else None

    def chart(self):
        if self.has_goal():
            line_chart = pygal.Line(truncate_legend=30)
            goals = self.goals_measurables(get_current_session(self.user))
            data = dict()
            for goal in goals:
                updates = models.UserGoalMeasurables.objects.filter(goal_measurable=goal)
                updates = sorted(updates, key=lambda u: u.session.date, reverse=True)
                data[goal.name] = {update.session.date: update.value if update.value != -1 else None for update in updates if update.session}

            all_dates = set()
            for updates in data.itervalues():
                for date in updates.iterkeys():
                    all_dates.add(date)
            all_dates = sorted(all_dates)

            for goal in data.iterkeys():
                updates = [data[goal][date] if date in data[goal] else None for date in all_dates]
                line_chart.add(goal, updates)

            line_chart.x_labels = map(str, all_dates)
            # line_chart.y_labels = [
            #     {'label':'Not Measured', 'value': -1},
            #     {'label': 'None', 'value': 0},
            #     {'label': 'Low', 'value': 1},
            #     {'label': 'Medium', 'value': 2},
            #     {'label': 'High', 'value': 3},
            # ]
            return line_chart.render(is_unicode=True, disable_xml_declaration=True)
        else:
            return None

    def goal_notes(self):
        notes = models.UserGoalNoteMeasurable.objects.filter(session=get_current_session(self.user), domain=self.domain_model)
        notes = sorted(notes, key=lambda n: n.session.date, reverse=True)
        data = []
        for note in notes:
            data.append({
                'updated': note.session.date,
                'notes': note.note,
                'id': str(uuid.uuid4())
            })
        return data

    def to_dict(self):
        return dict(
            measurables=self.measurables(),
            has_goals=self.has_goal(),
            past_measurables=self.past_measurables(),
            goals_measurables=self.goals_measurables(get_current_session(self.user)),
            chart=self.chart(),
            goal_notes=self.goal_notes(),
        )
