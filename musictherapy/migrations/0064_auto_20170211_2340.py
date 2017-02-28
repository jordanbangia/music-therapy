# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def replace_user_with_session_user(apps, schema_editor):
    user_goals_model = apps.get_model("musictherapy", "UserGoals")

    existing_ugs = set()
    for user_goal in user_goals_model.objects.all():
        try:
            session_user = user_goal.session.user
            if session_user:
                user_goal.user = session_user
                if (user_goal.goal, user_goal.user) not in existing_ugs:
                    user_goal.save()
                    existing_ugs.add((user_goal.goal, user_goal.user))
                else:
                    user_goal.delete()
        except AttributeError:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0063_auto_20161130_2009'),
    ]

    operations = [
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE', reverse_sql=migrations.RunSQL.noop),
        migrations.RunPython(replace_user_with_session_user),
        migrations.AlterField(
            model_name='usergoals',
            name='user',
            field=models.ForeignKey(to='musictherapy.UserInfo'),
        ),
        migrations.AlterUniqueTogether(
            name='usergoals',
            unique_together=set([('user', 'goal')]),
        ),
        migrations.RemoveField(
            model_name='usergoals',
            name='session',
        ),
        migrations.RunSQL(migrations.RunSQL.noop, reverse_sql='SET CONSTRAINTS ALL IMMEDIATE')
    ]
