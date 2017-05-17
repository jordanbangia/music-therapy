import calendar
import datetime
from collections import defaultdict

from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

import musictherapy.models as models
import musictherapy.utils as utils
from musictherapy.skills_data import SkillsData
from musictherapy.views import LOGIN_URL


@require_GET
@login_required(login_url=LOGIN_URL)
def assessment(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    music_pref = get_object_or_None(models.MusicalPreference, user=user)
    session = utils.current_session(user)

    domain_data = {
        'com': SkillsData("Communication", user, session),
        'pss': SkillsData("Psycho-Social", user, session),
        'phys': SkillsData("Physical", user, session),
        'cog': SkillsData("Cognitive", user, session),
        'music': SkillsData("Music", user, session),
        'aff': SkillsData("Affective", user, session),
    }

    return render(request, 'musictherapy/export/assessment.html', dict(
        userinfo=user,
        programs=get_user_programs(user),
        musical_preferences=music_pref,
        summary=get_summary_data(domain_data),
        domain_measurables=get_domain_measurables_and_goals(domain_data),
        date=datetime.datetime.now().date(),
    ))


@require_GET
@login_required(login_url=LOGIN_URL)
def treatment_plan(request, user_id,session_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    session = get_object_or_None(models.Session, pk=session_id)
    if not session:
        session = utils.current_session(user)

    domain_data = {
        'com': SkillsData("Communication", user, session),
        'pss': SkillsData("Psycho-Social", user, session),
        'phys': SkillsData("Physical", user, session),
        'cog': SkillsData("Cognitive", user, session),
        'music': SkillsData("Music", user, session),
        'aff': SkillsData("Affective", user, session),
    }

    export_data = dict()
    for domain, data in domain_data.iteritems():
        goals_data = defaultdict(list)
        for goal_measurable in data.goal_measurables:
            goals_data[goal_measurable.goal] += [goal_measurable]
        if len(goals_data) > 0:
            export_data[data.domain] = dict(goals_data)

    return render(request, 'musictherapy/export/treatment_plan.html', dict(
        pagesize="A4",
        userinfo=user,
        programs=get_user_programs(user),
        data=domain_data,
        date=datetime.datetime.now().date(),
        session=session,
        general_goals=SkillsData("General", user, session, prefix="general").user_goals,
        goals=export_data,
    ))


@require_GET
@login_required(login_url=LOGIN_URL)
def report(request, user_id, month, year):
    user = get_object_or_404(models.UserInfo, pk=user_id)

    month = int(month)
    year = int(year)
    _, end = calendar.monthrange(year, month)
    start_date = datetime.date(year=year, month=month, day=1)
    end_date = datetime.date(year=year, month=month, day=end)

    sessions = models.Session.objects.filter(date__gte=start_date, date__lte=end_date, user=user)

    notes = defaultdict(list)
    for session in sessions:
        if session.note is not None:
            notes[session.date].append(session.note)
        if session.status != 0:
            session_notes = [note.note for note in models.UserGoalNoteMeasurable.objects.filter(session=session) if note.note != '']
            if len(session_notes) > 0:
                notes[session.date] += session_notes
    notes = dict(notes)

    domain_data = {
        'com': SkillsData("Communication", user),
        'pss': SkillsData("Psycho-Social", user),
        'phys': SkillsData("Physical", user),
        'cog': SkillsData("Cognitive", user),
        'music': SkillsData("Music", user),
        'aff': SkillsData("Affective", user),
    }

    goals = dict()
    graphs = dict()
    for domain, data in domain_data.iteritems():
        goals_data = defaultdict(list)
        for goal_measurable in data.goal_measurables:
            goals_data[goal_measurable.goal] += [goal_measurable]
        if len(goals_data) > 0:
            goals[data.domain] = dict(goals_data)
        graphs[data.domain] = data.chart(start=start_date, end=end_date)

    return render(request, 'musictherapy/export/report.html', dict(
        userinfo=user,
        programs=get_user_programs(user),
        goals=goals,
        graphs=graphs,
        notes=notes,
        date=end_date,
        today=datetime.date.today(),
    ))


def get_summary_data(domain_data):
    summary_data = {data.domain: data.latest_summary_measurable() for data in domain_data.values()}

    for domain, summaries in summary_data.items():
        if summaries and 'fields' in summaries:
            summaries['fields'] = [field for field in summaries['fields'] if field not in ['Note', 'Updated']]
            summaries['data'] = list(reversed(summaries['data'][:4]))

    return summary_data


def get_domain_measurables_and_goals(domain_data):
    data = defaultdict(dict)
    for skill in domain_data.values():
        data[skill.domain] = format_data(skill.latest_user_measurables())
    return dict(data)


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
