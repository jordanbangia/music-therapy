from easy_pdf.views import PDFTemplateView
from django.shortcuts import get_object_or_404
from annoying.functions import get_object_or_None
import musictherapy.models as models
from collections import defaultdict
from musictherapy.skills_data import SkillsData


class MusicTherapyPDFView(PDFTemplateView):
    template_name = 'musictherapy/export.html'
    domain_data = None

    def get_context_data(self, **kwargs):
        user = get_object_or_404(models.UserInfo, pk=kwargs['user_id'])
        music_pref = get_object_or_None(models.MusicalPreference, user=user)

        com = SkillsData("Communication", user)
        pss = SkillsData("Psycho-Social", user)
        physical = SkillsData("Physical", user)
        cog = SkillsData("Cognitive", user)
        music = SkillsData("Music", user)
        affective = SkillsData("Affective", user)

        self.domain_data = {
            'com': com,
            'pss': pss,
            'phys': physical,
            'cog': cog,
            'music': music,
            'aff': affective
        }

        summary = self.get_summary_data()
        domain_data = self.get_domain_measurables_and_goals()

        return super(MusicTherapyPDFView, self).get_context_data(
            pagesize="A4",
            userinfo=user,
            musical_preferences=music_pref,
            summary=summary,
            domain_data=domain_data,
            **kwargs
        )

    def get_summary_data(self):
        summary_data = {data.domain: data.summary_measurable() for data in self.domain_data.values()}

        for domain, summaries in summary_data.items():
            if summaries and 'fields' in summaries:
                summaries['fields'] = [field for field in summaries['fields'] if field not in ['Note', 'Updated']]
                summaries['data'] = list(reversed(summaries['data'][:4]))

        return summary_data

    def get_domain_measurables_and_goals(self):
        data = defaultdict(dict)
        for skill in self.domain_data.values():
            data[skill.domain]['measurables'] = skill.get_all_measurables()
            data[skill.domain]['goals_measurables'] = skill.get_all_goal_measurables()
        return dict(data)
