import datetime
from collections import defaultdict
from pprint import pprint

from annoying.functions import get_object_or_None
from django.shortcuts import get_object_or_404
from easy_pdf.views import PDFTemplateView

import musictherapy.models as models
import musictherapy.utils as utils
from musictherapy.skills_data import SkillsData


class MusicTherapyAssessment(PDFTemplateView):
    template_name = 'musictherapy/export/assessment.html'
    domain_data = None

    def get_context_data(self, **kwargs):
        user = get_object_or_404(models.UserInfo, pk=kwargs['user_id'])
        music_pref = get_object_or_None(models.MusicalPreference, user=user)
        session = utils.current_session(user)

        self.domain_data = {
            'com': SkillsData("Communication", user, session),
            'pss': SkillsData("Psycho-Social", user, session),
            'phys': SkillsData("Physical", user, session),
            'cog': SkillsData("Cognitive", user, session),
            'music': SkillsData("Music", user, session),
            'aff': SkillsData("Affective", user, session),
        }

        summary = self.get_summary_data()
        domain_measurables = self.get_domain_measurables_and_goals()
        programs = get_user_programs(user)

        return super(MusicTherapyAssessment, self).get_context_data(
            pagesize="A4",
            userinfo=user,
            programs=programs,
            musical_preferences=music_pref,
            summary=summary,
            domain_measurables=domain_measurables,
            date=datetime.datetime.now().date(),
            **kwargs
        )

    def get_summary_data(self):
        summary_data = {data.domain: data.latest_summary_measurable() for data in self.domain_data.values()}

        for domain, summaries in summary_data.items():
            if summaries and 'fields' in summaries:
                summaries['fields'] = [field for field in summaries['fields'] if field not in ['Note', 'Updated']]
                summaries['data'] = list(reversed(summaries['data'][:4]))

        return summary_data

    def get_domain_measurables_and_goals(self):
        data = defaultdict(dict)
        for skill in self.domain_data.values():
            data[skill.domain] = format_data(skill.latest_user_measurables())
        return dict(data)


class MusicTherapyTreatmentPlan(PDFTemplateView):
    template_name = 'musictherapy/export/treatment_plan.html'
    domain_data = None

    def get_context_data(self, **kwargs):
        user = get_object_or_404(models.UserInfo, pk=kwargs['user_id'])
        session = utils.session_for_id(user, kwargs['session_id'])

        self.domain_data = {
            'com': SkillsData("Communication", user, session),
            'pss': SkillsData("Psycho-Social", user, session),
            'phys': SkillsData("Physical", user, session),
            'cog': SkillsData("Cognitive", user, session),
            'music': SkillsData("Music", user, session),
            'aff': SkillsData("Affective", user, session),
        }

        goals_data = dict()
        notes_data = dict()
        for domain, data in self.domain_data.iteritems():
            tmp = defaultdict(list)
            session_gms = data.session_goal_measurable_responses()
            for gm in data.goal_measurables:
                tmp[gm.goal] += [session_gms.get(gm.id, None)]

            if len(tmp) > 0:
                goals_data[data.domain] = dict(tmp)
                notes_data[data.domain] = data.session_goal_measurable_note().note

        return super(MusicTherapyTreatmentPlan, self).get_context_data(
            pagesize="A4",
            userinfo=user,
            programs=get_user_programs(user),
            data=self.domain_data,
            date=datetime.datetime.now().date(),
            session=session,
            general_goals=SkillsData("General", user, session, prefix="general").user_goals,
            goals=goals_data,
            notes=notes_data,
            **kwargs
        )


def get_user_programs(user):
    programs = []
    for program in user.program.all():
        programs.append('{}, {}'.format(program.location, program.name))
    return programs


def format_data(measurables):
    if measurables is None:
        return

    data = defaultdict(list)
    date = None
    for measurable in measurables:
        if not date:
            date = measurable.updated
        if isinstance(measurable, models.UserDomainNoteMeasurables):
            data["notes"] += [measurable]
        elif measurable.measurable.name is not None and measurable.value != -1:
            data[measurable.measurable.domain] += [measurable]
    data = dict(data)
    data['date'] = date
    return dict(data)