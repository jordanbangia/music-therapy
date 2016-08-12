# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Group, Permission, User
from django.db import migrations

from musictherapy.permissions import STAFF_PERMISSIONS, ADMIN_PERMISSIONS


def create_groups(apps, schema_editor):
    staff, created = Group.objects.get_or_create(name='Staff')

    for permission in STAFF_PERMISSIONS:
        p = Permission.objects.get(codename=permission)
        if p not in staff.permissions.all():
            staff.permissions.add(p)
    staff.save()

    admin, created = Group.objects.get_or_create(name='Admin')
    for permission in ADMIN_PERMISSIONS:
        p = Permission.objects.get(codename=permission)
        if p not in admin.permissions.all():
            admin.permissions.add(p)
    admin.save()


def add_default_users(apps, schema_editor):
    bd, created = User.objects.get_or_create(username='bdeimling')
    if created:
        bd.set_password('admin')
    bd.is_staff = True
    bd.is_superuser = True
    bd.is_active = True
    bd.save()

    rw, created = User.objects.get_or_create(username='rwatkiss')
    if created:
        rw.set_password('admin')
    rw.is_staff = True
    rw.is_active = True

    if not rw.groups.filter(name='Admin').exists():
        rw.groups.add(Group.objects.get(name='Admin'))
    rw.save()


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0027_auto_20160110_1224'),
    ]

    operations = [
        migrations.RunPython(create_groups),
        migrations.RunPython(add_default_users)
    ]
