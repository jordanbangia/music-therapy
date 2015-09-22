class Goals:
    # pscycho-social-skills
    PSS_RANGE_OF_AFFECT = 1
    PSS_SELF_ESTEEM = 2
    PSS_LEADERSHIP = 3
    PSS_RESTLESSNESS = 4
    PSS_PAIN_MANAGMENT = 5
    PSS_DECREASE_COMPULSIVE = 6
    PSS_DECREASE_DEPRESSIVE = 25
    PSS_INCREASE_TOLERANCE = 7
    PSS_INCREASE_ANXIETY_CONTROL = 8

    PSS_GOALS = (PSS_RANGE_OF_AFFECT, PSS_SELF_ESTEEM, PSS_LEADERSHIP, PSS_RESTLESSNESS,
                 PSS_PAIN_MANAGMENT, PSS_DECREASE_COMPULSIVE, PSS_DECREASE_DEPRESSIVE,
                 PSS_INCREASE_TOLERANCE, PSS_INCREASE_ANXIETY_CONTROL)

    # motor skills
    MTR_MOBILITY = 9
    MTR_FINE = 10
    MTR_GROSS = 11
    MTR_COORDINATION = 12

    MOTOR_GOALS = (MTR_COORDINATION, MTR_GROSS, MTR_FINE, MTR_MOBILITY)

    # communication
    COM_INCREASE_LEVEL = 13
    COM_INCREASE_SELF_EXPRESSION = 14

    COM_GOALS = (COM_INCREASE_LEVEL, COM_INCREASE_SELF_EXPRESSION)

    # cognition and memory
    COG_CHOICE_MAKING = 15
    COG_SENSORY_STIMULATION = 16
    COG_MAINTAIN_FUNCTION = 17
    COG_DECREASE_CONFUSION = 18
    COG_INCREASE_LEVEL_PART = 19

    COG_GOALS = (COG_CHOICE_MAKING, COG_SENSORY_STIMULATION, COG_MAINTAIN_FUNCTION, COG_DECREASE_CONFUSION,
                 COG_INCREASE_LEVEL_PART)

    # social skills
    SOC_ATTENTION_SPAN = 20
    SOC_ISOLATION = 21
    SOC_INTERACTION = 22

    SOC_GOALS = (SOC_ATTENTION_SPAN, SOC_ISOLATION, SOC_INTERACTION)

    # music skills
    MUS_MAINTAIN_KNOWLEDGE = 23
    MUS_MAINTAIN_SKILLS = 24

    MUS_GOALS = (MUS_MAINTAIN_SKILLS, MUS_MAINTAIN_KNOWLEDGE)

    GOALS_CHOICES = (
        (PSS_RANGE_OF_AFFECT, 'Increase range of affect'),
        (PSS_SELF_ESTEEM, 'Increase self-esteem'),
        (PSS_LEADERSHIP, 'Increase leadership role'),
        (PSS_RESTLESSNESS, 'Decrease restlessness'),
        (PSS_PAIN_MANAGMENT, 'Increase pain management'),
        (PSS_DECREASE_COMPULSIVE, 'Decrease compulsive/destructive behaviour'),
        (PSS_DECREASE_DEPRESSIVE, 'Decrease depressive symptoms'),
        (PSS_INCREASE_TOLERANCE, 'Increase frustration tolerance'),
        (PSS_INCREASE_ANXIETY_CONTROL, 'Increase anxiety control'),
        (MTR_MOBILITY, 'Stimulate and maintain mobility'),
        (MTR_FINE, 'Stimulate and maintain fine motor skills'),
        (MTR_GROSS, 'Stimulate and maintain gross motor skills'),
        (MTR_COORDINATION, 'Stimulate and maintain coordination'),
        (COM_INCREASE_LEVEL, 'Increase level of communication'),
        (COM_INCREASE_SELF_EXPRESSION, 'Increase self-expression'),
        (COG_CHOICE_MAKING, 'Increase choice making'),
        (COG_SENSORY_STIMULATION, 'Increase sensory stimulation'),
        (COG_MAINTAIN_FUNCTION, 'Maintain cognitive function'),
        (COG_DECREASE_CONFUSION, 'Decrease confusion and disorientation'),
        (COG_INCREASE_LEVEL_PART, 'Increase level of participation'),
        (SOC_ATTENTION_SPAN, 'Increase attention span'),
        (SOC_ISOLATION, 'Decrease isolation'),
        (SOC_INTERACTION, 'Increase social interaction'),
        (MUS_MAINTAIN_KNOWLEDGE, 'Maintain current knowledge of music'),
        (MUS_MAINTAIN_SKILLS, 'Maintain current music skills'),
    )

    @staticmethod
    def in_list(selection, goals):
        for choice in selection:
            if int(choice) in goals:
                return True
        return False

    @staticmethod
    def intersection(list1, list2):
        ret = []
        if list1:
            for item in list1:
                if int(item) in list2:
                    ret.append(int(item))
        return ret

    @staticmethod
    def has_psycho_social_goals(user):
        selection = user.goals
        if selection is None:
            return False
        return Goals.in_list(selection, Goals.PSS_GOALS)

    @staticmethod
    def has_motor_goals(user):
        selection = user.goals
        if selection is None:
            return False
        return Goals.in_list(selection, Goals.MOTOR_GOALS)

    @staticmethod
    def has_communication_goals(user):
        selection = user.goals
        if selection is None:
            return False
        return Goals.in_list(selection, Goals.COM_GOALS)

    @staticmethod
    def has_cognition_goals(user):
        selection = user.goals
        if selection is None:
            return False
        return Goals.in_list(selection, Goals.COG_GOALS)

    @staticmethod
    def has_social_goals(user):
        selection = user.goals
        if selection is None:
            return False
        return Goals.in_list(selection, Goals.SOC_GOALS)

    @staticmethod
    def has_music_goals(user):
        selection = user.goals
        if selection is None:
            return False
        return Goals.in_list(selection, Goals.MUS_GOALS)

    @staticmethod
    def get_communication_goals(user):
        return Goals.intersection(user.goals, Goals.COM_GOALS)

    @staticmethod
    def get_psycho_social_goals(user):
        return Goals.intersection(user.goals, Goals.PSS_GOALS)