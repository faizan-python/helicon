# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20160222_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='complete_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='tax',
            field=models.FloatField(default=0),
        ),
    ]
