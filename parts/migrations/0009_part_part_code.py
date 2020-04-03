# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0008_auto_20170205_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='part_code',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
