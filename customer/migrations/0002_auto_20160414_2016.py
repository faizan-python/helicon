# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_picture_icon',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_picture_macroicon',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_picture_thumbnail',
        ),
        migrations.AddField(
            model_name='customer',
            name='tin_no',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
