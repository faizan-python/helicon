# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20160223_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='advance_amount',
            field=models.FloatField(default=0),
        ),
    ]
