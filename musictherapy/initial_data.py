#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")

from annoying.functions import get_object_or_None

import musictherapy.models as models

DOMAINS = ['Physical', 'Communication', 'Cognitive', 'Psycho-Social', 'Affective', 'Music', 'General']

SUB_DOMAINS = {
    'Communication': ['Verbal Skills', 'Receptive Language', 'Singing/Vocal Skills'],
    'Cognitive': ['Comprehension', 'Visual Perception', 'Auditory Perception', 'Laterality and Directionality',
                  'Short-Term Memory', 'Long-Term Memory'],
    'Physical': ['Mobility', 'Fine Motor', 'Gross Motor', 'Coordination', 'Limitations'],
    'Music': ['Rhythm/Beat', 'Melody/Tonal', 'Interest/Preference'],
    'Psycho-Social': ['Interactions', 'Attending Skills', 'Sharing and Turn-Taking', 'Participation in Group Music Therapy'],
    'Affective': ['Inappropriate Emotional Response', 'Appropriate Emotional Response']
}

GOALS = {
    'General': ['To provide a productive use of time', 'To aid relaxation', 'To improve quality of life by alleviation of loneliness',
                'To improve quality of life by providing dignity', 'To improve quality of life by providing validation of self', 'To improve quality of life by providing sensory stimulation'],
    'Communication': ['Increase level of communication'],
    'Cognitive': ['Increase choice making', 'Maintain cognitive function', 'Decrease confusion and disorientation'],
    'Mobility': ['Stimulate and maintain mobility'],
    'Fine Motor': ['Stimulate and maintain fine motor skills'],
    'Gross Motor': ['Stimulate and maintain gross motor skills'],
    'Coordination': ['Stimulate and maintain coordination'],
    'Music': ['Maintain current knowledge of music', 'Maintain current music skills'],
    'Psycho-Social': ['Increase attention span', 'Decrease isolation', 'Increase social interaction'],
    'Affective': ['Decrease restlessness', 'Increase pain management', 'Increase leadership role', 'Decrease depressive symptoms', 'Increase frustration tolerance',
                  'Decrease level of anxiety', 'Decrease catastrophic reactions']
}

SUB_GOALS = {
    'To provide a productive use of time': ['By creating a personalized playlist for listening enjoyment', 'By encouraging musical engagement in previous or emerging talent'],
    'To aid relaxation': ['By providing a personalized playlist to listen to', 'By participation in relaxation program'],
    'To improve quality of life by alleviation of loneliness': ['By providing one-on-one time interacting through music', 'By including in group for music listening enjoyment'],
    'To improve quality of life by providing validation of self': ['By including in group for music listening enjoyment', 'By enabling participation in programs'],
    'To improve quality of life by providing sensory stimulation': ['By providing stimulation through music listening and participation']
}

DOMAINS_MEASURABLES = {
    'Verbal Skills': [('Appropriate rate of speech', True), ('Appropriate pronunciation', True), ('Engage in conversation', True), ('Communicates with single words (1), phrases (2), full sentences (3)', True),
                      ('Appropriate Communication', True), ('Word finding difficulty', False)],
    'Receptive Language': [('Follow directions', True), ('Responds to verbal instructions', True), ('Responds to name in song', True), ('Responds to Hello and Goodbye', True)],
    'Singing/Vocal Skills': [('Call and response/imitation', True), ('Singing familiar songs', True)],
    'Comprehension': [('Ability to recognize error and self-control', True), ('Ability to make choices', True), ('Hallucinations', False), ('Hoarding', False), ('Delusions', False), ('Able to organize thoughts', True)],
    'Visual Perception': [('Read a song sheet/book', True)],
    'Auditory Perception': [('Awareness in changes in dynamics', True), ('Awareness of changes in tempo', True), ('Awareness in changes in pitch', True)],
    'Laterality and Directionality': [('Know directions (right, left, forward, back, up, down)', True), ('Follows hand-over-hand directions', True)],
    'Short-Term Memory': [('Oriented time', True), ('Oriented place', True)],
    'Long-Term Memory': [('Recalls lyrics from familiar songs', True), ('Recalls own name', True), ('Recalls name of familiar persons', True), ('Recalls melody from familiar songs', True)],
    'Mobility': [('Independent mobility', True), ('Gait', True), ('Endurance', True), ('Structure dance', True)],
    'Fine Motor': [('Grasps instruments/mallets', True), ('Demonstrates finger independence', True)],
    'Gross Motor': [('Demonstrates upper extremity control', True), ('Range of Motion', True), ('Crosses midline', True), ('Reaches for instrument', True)],
    'Coordination': [('Demonstrates adequate eye-hand coordination', True), ('Demonstrated adequate body coordination', True)],
    'Limitations': [('Hearing', True), ('Sight', True)],
    'Rhythm/Beat': [('Match rhythm', True), ('Keep steady beat', True), ('Adapt to rhythmic changes', True)],
    'Melody/Tonal': [('Match pitch', True), ('Discriminates dynamics', True), ('Discriminates duration', True), ('Sing familiar songs', True), ('Finish music phrases', True)],
    'Interest/Preference': [('Responds to music', True), ('Chooses a song or style', True), ('Identifies familiar song titles when given melody only', True),
                            ('Identifies familiar song titles when given song lyrics', True)],
    'Interactions': [('Engages in imitation, parallel, or interactive music making', True), ('Passes/shares instruments', True), ('Converses with others', True), ('Dances with others', True)],
    'Attending Skills': [('Makes and/or maintains eye contact', True), ('Remains on task for duration', True), ('Attends to task', True)],
    'Sharing and Turn-Taking': [('Passes/exchanges instruments with others', True), ('Plays in response to name', True)],
    'Participation in Group Music Therapy': [('Active in session', True), ('Remain in group', True), ('Accept leadership', True), ('Disruptive',  False), ('Resistive', False), ('Sleeping', False),
                                             ('Territorial', False), ('Isolated', False), ('Uncooperative', False), ('Repetitive', False), ('Questioning', False), ('Wandering', False)],
    'Inappropriate Emotional Response': [('Agitation', False), ('Ambivalent', False), ('Anxiety', False), ('Assertive', False), ('Catastrophic reactions', False), ('Depressed', False), ('Express or exhibits pain', False),
                                         ('Fearful', False), ('Frustration', False), ('Inappropriate sexual behaviour', False), ('Labile', False), ('Withdrawn', False), ('Restless', False), ('Self-abusive', False), ('Self-stimulative', False)],
    'Appropriate Emotional Response': [('Self-esteem', True), ('Range of affect', True), ('Sense of humour', True)]
}

GOAL_MEASURABLES = {
    'Increase level of communication': ['Verbal participation with verbal prompt', 'Verbal participation without verbal prompt'],
    'Increase choice making': ['Choice was made verbally', 'Choice was made nonverbally'],
    'Maintain cognitive function': ['Questions were answered', 'Long-term memory retrieval', 'Short-term memory retrieval'],
    'Decrease confusion and disorientation': ['Confusion or disorientation'],
    'Stimulate and maintain mobility': ['Successful participation in mobility activity'],
    'Stimulate and maintain fine motor skills': ['Successful participation in fine motor activity'],
    'Stimulate and maintain gross motor skills': ['Successful participation in gross motor activity'],
    'Stimulate and maintain coordination': ['Successful participation in coordination activity'],
    'Maintain current knowledge of music': ['Music trivia answered correctly', 'Song known without lyrics', 'Song known without title', 'Song known'],
    'Maintain current music skills': ['Music skill demonstrated', 'Opinions given'],
    'Increase attention span': ['Redirection was required', 'Encouragement to stay in program required'],
    'Decrease isolation': ['Participation in program', 'Joining of program'],
    'Increase social interaction': ['Interaction with staff', 'Interaction with peers', 'Interaction with therapist'],
    'Decrease restlessness': ['Stay in program'],
    'Increase pain management': ['Complained about pain'],
    'Increase leadership role': ['Refused to lead program', 'Led program'],
    'Decrease depressive symptoms': ['Depressive symptoms displayed'],
    'Increase frustration tolerance': ['Frustration was displayed'],
    'Decrease level of anxiety': ['Anxiety was displayed'],
    'Decrease catastrophic reactions': ['Reactions occurred'],
    'To provide a productive use of time': ['By creating a personalized playlist for listening enjoyment', 'By encouraging musical engagement in previous or emerging talent'],
    'To aid relaxation': ['By providing a personalized playlist to listen to', 'By participation in a relaxation program'],
    'To improve quality of life by alleviation of loneliness': ['By providing one-on-one time interacting through music', 'By including in group for music listening enjoyment'],
    'To improve quality of life by providing validation of self': ['By including in group for music listening enjoyment', 'By enabling participation in programs'],
    'To improve quality of life by providing sensory stimulation': ['By providing stimulation through muisc listening and participation'],
}


COMPLETED = dict()


def insert_initial_data():
    # domains
    for domain in DOMAINS:
        d = get_object_or_None(models.Domains, name=domain)
        if not d:
            d = models.Domains.objects.create(name=domain, enabled=1)
            d.save()
        COMPLETED[domain] = d

    for parent_domain in SUB_DOMAINS:
        for sub_domain in SUB_DOMAINS[parent_domain]:
            d = get_object_or_None(models.Domains, name=sub_domain)
            if not d:
                d = models.Domains.objects.create(name=sub_domain, enabled=1, parent=COMPLETED[parent_domain])
                d.save()
            COMPLETED[sub_domain] = d

    for domain in GOALS:
        for goal in GOALS[domain]:
            g = get_object_or_None(models.Goals, name=goal)
            if not g:
                g = models.Goals.objects.create(name=goal, enabled=1, domain=COMPLETED[domain])
                g.save()
            COMPLETED[goal] = g

    for goal in SUB_GOALS:
        for sub_goal in SUB_GOALS[goal]:
            g = get_object_or_None(models.Goals, name=goal)
            if not g:
                g = models.Goals.objects.create(name=sub_goal, enabled=1, domain=COMPLETED[goal].domain, parent=COMPLETED[goal])
                g.save()

    for domain in DOMAINS_MEASURABLES:
        for measurable, is_positive in DOMAINS_MEASURABLES[domain]:
            m = get_object_or_None(models.DomainMeasurables, name=measurable)
            if not m:
                m = models.DomainMeasurables.objects.create(name=measurable, enabled=1, domain=COMPLETED[domain], pos_neg=1 if is_positive else -1)
                m.save()

    for goal, measurables in GOAL_MEASURABLES.iteritems():
        for measurable in measurables:
            m = get_object_or_None(models.GoalsMeasurables, name=measurable)
            if not m:
                m = models.GoalsMeasurables.objects.create(name=measurable, enabled=1, goal=COMPLETED[goal])
                m.save()
    return


if __name__ == "__main__":
    insert_initial_data()
