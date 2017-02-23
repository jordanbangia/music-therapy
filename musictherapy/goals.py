from musictherapy.skills_data import SkillsData


def get_skills_data_for_user_as_list(user, session):
    return [
        SkillsData("Communication", user, session),
        SkillsData("Psycho-Social", user, session),
        SkillsData("Physical", user, session),
        SkillsData("Cognitive", user, session),
        SkillsData("Music", user, session),
        SkillsData("Affective", user, session),
    ]


def get_skills_data_for_user_as_dict(user, session):
    return {
        'com': SkillsData("Communication", user, session),
        'pss': SkillsData("Psycho-Social", user, session),
        'phys': SkillsData("Physical", user, session),
        'cog': SkillsData("Cognitive", user, session),
        'mus': SkillsData("Music", user, session),
        'aff': SkillsData("Affective", user, session),
    }
