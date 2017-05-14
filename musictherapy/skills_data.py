import uuid
from collections import defaultdict

import pygal
from annoying.functions import get_object_or_None
from django.utils.functional import cached_property
from silk.profiling.profiler import silk_profile

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
    def __init__(self, domain, user, session=None, prefix=None):
        self.user = user
        self.session = session
        self.domain = domain
        self.domain_model = get_object_or_None(models.Domains, name=self.domain)
        self.goals = models.Goals.objects.filter(domain__in=self.domains, enabled=1)
        self.prefix = SKILLS_PREFIX_DICT[domain] if not prefix else prefix

    @cached_property
    def measurables(self):
        with silk_profile(name='Get measurables {}, {}'.format(self.user.pk, self.domain)):
            measurables = defaultdict(list)
            for measurable in models.DomainMeasurables.objects.filter(domain__in=self.domains, enabled=1):
                measurables[measurable.domain.name] += [measurable]
            return dict(measurables)

    @cached_property
    def domains(self):
        with silk_profile(name='Get domains {}, {}'.format(self.user.pk, self.domain)):
            domains = [self.domain_model]
            if self.domain_model:
                domains += models.Domains.objects.filter(parent=self.domain_model, enabled=1)
            return domains

    @cached_property
    def sub_domains(self):
        with silk_profile(name='Get subdomains {}, {}'.format(self.user.pk, self.domain)):
            return [domain for domain in self.domains if domain.parent == self.domain_model]

    @cached_property
    def user_goals(self):
        with silk_profile(name='Get user goals {}, {}'.format(self.user.pk, self.domain)):
            return models.UserGoals.objects.filter(goal__in=self.goals, user=self.user)

    @cached_property
    def goal_measurables(self):
        with silk_profile(name='Get goal measurables {}, {}'.format(self.user.pk, self.domain)):
            return models.GoalsMeasurables.objects.filter(goal__in=[ug.goal for ug in self.user_goals], enabled=1)

    @cached_property
    def user_measurables(self):
        with silk_profile(name='Get user measurables {}, {}'.format(self.user.pk, self.domain)):
            return models.UserMeasurables.objects.filter(user=self.user)

    @cached_property
    def user_domain_note_measurables(self):
        with silk_profile(name='Get user domain note measurables {}, {}'.format(self.user.pk, self.domain)):
            return models.UserDomainNoteMeasurables.objects.filter(user=self.user, domain=self.domain_model)

    @cached_property
    def user_goal_measurables(self):
        with silk_profile(name='Get user goal measurables {}, {}'.format(self.user.pk, self.domain)):
            return models.UserGoalMeasurables.objects.filter(session__user=self.user)

    @cached_property
    def user_goal_note_measurables(self):
        with silk_profile(name='Get user note measurables {}, {}'.format(self.user.pk, self.domain)):
            return models.UserGoalNoteMeasurable.objects.filter(session__user=self.user, domain=self.domain_model)

    @cached_property
    def has_goal(self):
        with silk_profile(name='Get has goals {}, {}'.format(self.user.pk, self.domain)):
            return len(self.user_goals) > 0

    @cached_property
    def session_goal_measurable_responses(self):
        with silk_profile(name='Get goal measurable responses for session {}, {}'.format(self.user.pk, self.domain)):
            if not self.session:
                return {}
            return {measurable.goal_measurable.id: measurable for measurable in self.user_goal_measurables if self.session == measurable.session and measurable.goal_measurable in self.goal_measurables}

    @cached_property
    def custom_goals(self):
        with silk_profile(name='Get custom goals {}, {}'.format(self.user.pk, self.domain)):
            goals = [goal for goal in self.goals if goal.is_custom == 1 and goal.user == self.user]
            return goals

    def all_user_measurables(self):
        with silk_profile(name='Get all user measurables {}, {}'.format(self.user.pk, self.domain)):
            user_measurables = self.user_measurables
            notes = self.user_domain_note_measurables

            past_measurables = defaultdict(list)
            for um in user_measurables:
                if um.measurable.domain in self.domains:
                    past_measurables[um.updated] += [um]

            for note in notes:
                past_measurables[note.updated] += [note]

            return dict(past_measurables)

    def latest_user_measurables(self, as_dict=False):
        with silk_profile(name='Get latest user measurables {}, {}'.format(self.user.pk, self.domain)):
            measurables = self.all_user_measurables()
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

    def past_measurables(self, is_summary=False):
        with silk_profile(name='Get past measurables {}, {}'.format(self.user.pk, self.domain)):
            past_measurables = self.all_user_measurables()

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
                data['fields'] = [sub_domain.name for sub_domain in self.sub_domains] + ['Updated', 'Note']
                if is_summary and self.domain != 'Affective':
                    data['fields'] += ['Total']
                data['data'] = sorted(data['data'], key=lambda field: field['Updated'], reverse=True)
                return data
            return None

    # used for pdf export
    def latest_summary_measurable(self):
        with silk_profile(name='Get latest summary measurables {}, {}'.format(self.user.pk, self.domain)):
            past_measurables = self.past_measurables(is_summary=True)
            if past_measurables:
                past_measurables['data'] = past_measurables['data'][:1]
            return past_measurables

    def chart(self, start=None, end=None):
        with silk_profile(name='Get charts {}, {}'.format(self.user.pk, self.domain)):
            if self.has_goal:
                line_chart = pygal.Line(truncate_legend=30, range=(0, 3), max_scale=3, min_scale=3)
                goals = self.goal_measurables
                data = dict()
                for goal in goals:
                    updates = [measurable for measurable in self.user_goal_measurables if measurable.goal_measurable == goal]
                    updates = sorted(updates, key=lambda u: u.session.date, reverse=True)
                    data[goal.name] = {update.session.date: update.value if update.value != -1 else None for update in updates if update.session}

                all_dates = set()
                for updates in data.itervalues():
                    for date in updates.iterkeys():
                        if start is None or date <= start:
                            continue
                        if end is None or date >= end:
                            continue
                        all_dates.add(date)
                all_dates = sorted(all_dates)

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

    @cached_property
    def goal_notes(self):
        with silk_profile(name='Get goal notes {}, {}'.format(self.user.pk, self.domain)):
            return sorted(self.user_goal_note_measurables, key=lambda n: n.session.date, reverse=True)

    def session_goal_measurable_note(self):
        with silk_profile(name='Get session goal measurable notes {}, {}'.format(self.user.pk, self.domain)):
            if not self.session:
                return None
            notes = self.goal_notes
            session_notes = [note for note in notes if note.session == self.session]
            return session_notes[0] if len(session_notes) > 0 else None

    def to_dict(self, program_data_only=False):
        data = dict(
            domain=self.domain,
            has_goals=self.has_goal,
            goals_measurables=self.goal_measurables,
            goal_notes=self.goal_notes,
            session_goal_measurables_response=self.session_goal_measurable_responses,
            session_goal_measurables_note=self.session_goal_measurable_note(),
            prefix=self.prefix,
            custom_goals=self.custom_goals,
        )

        if not program_data_only:
            data.update(dict(
                measurables=self.measurables,
                summary_measurable=self.past_measurables(is_summary=True),
                past_measurables=self.past_measurables(),
                latest_measurables=self.latest_user_measurables(as_dict=True),
                chart=self.chart(),
            ))
        return data
