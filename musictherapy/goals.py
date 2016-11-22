from musictherapy.skills_data import SkillsData


def get_session_goals(session, user):
    session_goals = {data.domain: data.goals_measurables(session) for data in get_skills_data_for_user_as_list(user)}

    if all(len(gms) == 0 for domain, gms in session_goals.iteritems()):
        return None
    return session_goals


def get_custom_goals(session, user):
    return {data.domain: data.custom_goals(session) for data in get_skills_data_for_user_as_list(user)}


def get_skills_data_for_user_as_list(user):
    return [
        SkillsData("Communication", user),
        SkillsData("Psycho-Social", user),
        SkillsData("Physical", user),
        SkillsData("Cognitive", user),
        SkillsData("Music", user),
        SkillsData("Affective", user),
    ]


def get_skills_data_for_user_as_dict(user):
    return {
        'com': SkillsData("Communication", user),
        'pss': SkillsData("Psycho-Social", user),
        'phys': SkillsData("Physical", user),
        'cog': SkillsData("Cognitive", user),
        'mus': SkillsData("Music", user),
        'aff': SkillsData("Affective", user),
    }
