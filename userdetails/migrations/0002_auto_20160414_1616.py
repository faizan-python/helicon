# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture_icon',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture_macroicon',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture_thumbnail',
        ),
    ]
