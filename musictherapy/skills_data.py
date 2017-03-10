import uuid
from collections import defaultdict

import pygal
from annoying.functions import get_object_or_None
from django.utils.functional import cached_property

import musictherapy.models as models
import musictherapy.utils as utils

SKILLS_PREFIX_DICT = {
    'Communication': 'com',
    'Psycho-Social': 'pss',
    'Physical': 'phys',
    'Cognitive': 'cog',
    'Music': 'mus',
    'Affective': 'aff'
}


def prefix_to_domain(prefix):
    if prefix in SKILLS_PREFIX_DICT.values():
        return [domain for domain, domain_prefix in SKILLS_PREFIX_DICT.iteritems() if domain_prefix == prefix][0]
    return None


class SkillsData(object):
    def __init__(self, domain, user, session, prefix=None):
        self.user = user
        self.session = session
        self.domain = domain
        self.domain_model = get_object_or_None(models.Domains, name=self.domain)
        self.goals = models.Goals.objects.filter(domain__in=self.domains, enabled=1)
        self.prefix = SKILLS_PREFIX_DICT[domain] if not prefix else prefix

    @cached_property
    def measurables(self):
        measurables = defaultdict(list)
        for measurable in models.DomainMeasurables.objects.filter(domain__in=self.domains, enabled=1):
            measurables[measurable.domain.name] += [measurable]
        return dict(measurables)

    @cached_property
    def domains(self):
        domains = [self.domain_model]
        if self.domain_model:
            domains += models.Domains.objects.filter(parent=self.domain_model, enabled=1)
        return domains

    def sub_domains(self):
        return [domain for domain in self.domains if domain.parent == self.domain_model]

    @cached_property
    def user_goals(self):
        return models.UserGoals.objects.filter(goal__in=self.goals, user=self.user)

    @cached_property
    def goal_measurables(self):
        return models.GoalsMeasurables.objects.filter(goal__in=[ug.goal for ug in self.user_goals], enabled=1)

    def has_goal(self):
        return len(self.user_goals) > 0

    def session_goal_measurable_responses(self):
        return {measurable.goal_measurable.id: measurable for measurable in models.UserGoalMeasurables.objects.filter(session=self.session, goal_measurable__in=self.goal_measurables)}

    def custom_goals(self):
        goals = models.Goals.objects.filter(domain__in=self.domains, enabled=1, is_custom=1, user=self.user)
        user_goals = models.UserGoals.objects.filter(goal__in=goals, user=self.user)
        return [ug.goal for ug in user_goals]

    def all_user_measurables(self):
        user_measurables = models.UserMeasurables.objects.filter(user=self.user)
        notes = models.UserDomainNoteMeasurables.objects.filter(user=self.user, domain=self.domain_model)

        past_measurables = defaultdict(list)
        for um in user_measurables:
            if um.measurable.domain in self.domains:
                past_measurables[um.updated] += [um]

        for note in notes:
            past_measurables[note.updated] += [note]

        return dict(past_measurables)

    def latest_user_measurables(self):
        measurables = self.all_user_measurables()
        dates = sorted(measurables.keys(), reverse=True)
        return measurables[dates[0]] if len(dates) > 0 else None

    def past_measurables(self, is_summary=False):
        past_measurables = self.all_user_measurables()

        data = dict(data=[])
        for date, data_list in past_measurables.iteritems():
            sub_domain_value = defaultdict(list)
            note = None
            for um in data_list:
                if isinstance(um, models.UserDomainNoteMeasurables):
                    note = um.note
                elif um.value != -1:
                    sub_domain_value[um.measurable.domain.name] += [um.value*um.measurable.pos_neg]

            all_values = []
            for sub_domain, values in sub_domain_value.iteritems():
                if is_summary and self.domain != 'Affective':
                    all_values += values
                sub_domain_value[sub_domain] = sum(values) * 100 / float(len(values) * 3) if len(values) > 0 else None
            if is_summary:
                sub_domain_value['Total'] = sum(all_values) * 100 / float(len(all_values) * 3) if len(all_values) > 0 else '--'
            sub_domain_value['id'] = str(uuid.uuid4())
            sub_domain_value['Note'] = note
            sub_domain_value['Updated'] = date
            data['data'].append(dict(sub_domain_value))

        if len(data['data']) > 0:
            data['fields'] = [sub_domain.name for sub_domain in self.sub_domains()] + ['Updated', 'Note']
            if is_summary and self.domain != 'Affective':
                data['fields'] += ['Total']
            data['data'] = sorted(data['data'], key=lambda field: field['Updated'], reverse=True)
            return data
        return None

    def latest_summary_measurable(self):
        past_measurables = self.past_measurables(is_summary=True)
        if past_measurables:
            past_measurables['data'] = past_measurables['data'][:1]
        return past_measurables

    def latest_goals_measurables(self, return_model=False):
        goals = self.goal_measurables
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

        notes = models.UserGoalNoteMeasurable.objects.filter(session=utils.latest_session(self.user), domain=self.domain_model)
        return {'data': data, 'notes': notes} if len(data) > 0 or len(notes) > 0 else None

    def chart(self):
        if self.has_goal:
            line_chart = pygal.Line(truncate_legend=30)
            goals = self.goal_measurables
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
            return line_chart.render(is_unicode=True, disable_xml_declaration=True)
        else:
            return None

    @cached_property
    def goal_notes(self):
        notes = models.UserGoalNoteMeasurable.objects.filter(session__user=self.user, domain=self.domain_model)
        return sorted(notes, key=lambda n: n.session.date, reverse=True)

    def session_goal_measurable_note(self):
        notes = self.goal_notes
        session_notes = [note for note in notes if note.session == self.session]
        return session_notes[0] if len(session_notes) > 0 else None

    def to_dict(self):
        return dict(
            domain=self.domain,
            measurables=self.measurables,
            has_goals=self.has_goal(),
            past_measurables=self.past_measurables(),
            goals_measurables=self.goal_measurables,
            chart=self.chart(),
            goal_notes=self.goal_notes,
            summary_measurable=self.past_measurables(is_summary=True),
            session_goal_measurables_response=self.session_goal_measurable_responses(),
            session_goal_measurables_note=self.session_goal_measurable_note(),
            prefix=self.prefix,
            custom_goals=self.custom_goals()
        )
