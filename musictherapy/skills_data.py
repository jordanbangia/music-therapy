import uuid
from collections import defaultdict

import pygal
from annoying.functions import get_object_or_None
from django.utils.functional import cached_property

import musictherapy.models as models
from musictherapy import utils

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
    def __init__(self, domain, user, session=None, prefix=None):
        self.user = user
        self.session = session
        self.domain = domain
        self.prefix = SKILLS_PREFIX_DICT[domain] if not prefix else prefix
        self.domain_model = get_object_or_None(models.Domains, name=self.domain)

    def measurables(self):
        measurables = defaultdict(list)
        for measurable in models.DomainMeasurables.objects.filter(domain__in=self.domains, enabled=1):
            measurables[measurable.domain.name] += [measurable]
        return dict(measurables)

    @cached_property
    def domain_goals(self):
        return models.Goals.objects.filter(domain__in=self.domains, enabled=1)

    @cached_property
    def domains(self):
        if self.domain_model:
            domains = [self.domain_model] + list(models.Domains.objects.filter(parent=self.domain_model, enabled=1))
            return domains
        return []

    def sub_domains(self):
        return models.Domains.objects.filter(parent=self.domain_model, enabled=1)

    @cached_property
    def goal_measurables(self):
        return models.GoalsMeasurables.objects.filter(goal__in=self.domain_goals, enabled=1)

    @cached_property
    def user_measurables(self):
        return models.UserMeasurables.objects.filter(user=self.user, measurable__domain__in=self.domains)

    @cached_property
    def user_domain_note_measurables(self):
        return models.UserDomainNoteMeasurables.objects.filter(user=self.user, domain=self.domain_model)

    @cached_property
    def user_goal_measurables(self):
        return models.UserGoalMeasurables.objects.filter(session__user=self.user)

    def has_goal(self):
        return models.UserGoals.objects.filter(goal__in=self.domain_goals, user=self.user).count() > 0

    def session_goal_measurable_responses(self):
        if not self.session:
            return {}
        return {measurable.goal_measurable.id: measurable for measurable in models.UserGoalMeasurables.objects.filter(session=self.session, goal_measurable__in=self.goal_measurables)}

    def custom_goals(self):
        return models.Goals.objects.filter(domain__in=self.domains, enabled=1, user=self.user, is_custom=1)

    @cached_property
    def all_user_measurables(self):
        past_measurables = defaultdict(list)
        for um in self.user_measurables:
            past_measurables[um.updated] += [um]
        for note in self.user_domain_note_measurables:
            past_measurables[note.updated] += [note]
        return dict(past_measurables)

    def latest_user_measurables(self, as_dict=False):
        measurables = self.all_user_measurables
        dates = sorted(measurables.keys(), reverse=True)
        measurables = measurables[dates[0]] if len(dates) > 0 else None
        if as_dict:
            if measurables is None:
                return dict()
            note = measurables[-1]  # note will be the last element if its included
            measurables = {um.measurable.id: um for um in measurables if isinstance(um, models.UserMeasurables)}
            if isinstance(note, models.UserDomainNoteMeasurables):
                measurables['note'] = note
        return measurables

    def _past_measurables(self, is_summary=False):
        past_measurables = self.all_user_measurables

        data = dict(data=[])
        for date, data_list in past_measurables.iteritems():
            sub_domain_value = defaultdict(list)
            note = None
            for um in data_list:
                if isinstance(um, models.UserDomainNoteMeasurables):
                    note = um.note
                elif um.value != -1:
                    sub_domain_value[um.measurable.domain.name] += [um.value * um.measurable.pos_neg]

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

    @cached_property
    def past_measurables(self):
        return self._past_measurables(is_summary=False)

    @cached_property
    def past_summary_measurables(self):
        return self._past_measurables(is_summary=True)

    # used for pdf export
    def latest_summary_measurable(self):
        past_measurables = self.past_summary_measurables
        if past_measurables:
            past_measurables['data'] = past_measurables['data'][:1]
        return past_measurables

    def chart(self, start=None, end=None):
        if self.has_goal:
            line_chart = pygal.Line(truncate_legend=30, range=(0, 3), max_scale=3, min_scale=3)
            data = dict()
            for goal in self.goal_measurables:
                updates = [measurable for measurable in self.user_goal_measurables if measurable.goal_measurable == goal and
                           utils.is_date_in_range(measurable.session.date, start=start, end=end)]
                updates = sorted(updates, key=lambda up: up.session.date, reverse=True)
                data[goal.name] = {update.session.date: update.value if update.value != -1 else None for update in updates if update.session}

            all_dates = sorted(set([d for u in data.itervalues() for d in u.iterkeys()]))

            for goal in data.iterkeys():
                updates = [data[goal][date] if date in data[goal] else None for date in all_dates]
                if len(updates) > 0:
                    line_chart.add(goal, updates)

            if len(line_chart.raw_series) == 0:
                return None
            line_chart.x_labels = map(str, all_dates)
            line_chart.y_labels = [
                {'value': 0, 'label': 'None'},
                {'value': 1, 'label': 'Low'},
                {'value': 2, 'label': 'Medium'},
                {'value': 3, 'label': 'High'},
            ]
            return line_chart.render(is_unicode=True, disable_xml_declaration=True)
        else:
            return None

    def goal_notes(self):
        return models.UserGoalNoteMeasurable.objects.filter(session__user=self.user, domain=self.domain_model).order_by('-session__date')

    def session_goal_measurable_note(self):
        if not self.session:
            return None
        return models.UserGoalNoteMeasurable.objects.filter(session=self.session, domain=self.domain_model).order_by('-session__date').first()

    def to_dict(self, program_data_only=False):
        data = dict(
            domain=self.domain,
            has_goals=self.has_goal(),
            goals_measurables=self.goal_measurables,
            goal_notes=self.goal_notes(),
            session_goal_measurables_response=self.session_goal_measurable_responses(),
            session_goal_measurables_note=self.session_goal_measurable_note(),
            prefix=self.prefix,
            custom_goals=self.custom_goals(),
        )

        if not program_data_only:
            data.update(dict(
                measurables=self.measurables(),
                summary_measurable=self.past_summary_measurables,
                past_measurables=self.past_measurables,
                latest_measurables=self.latest_user_measurables(as_dict=True),
                chart=self.chart(),
            ))
        return data
