# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_labourcost'),
        ('service', '0009_auto_20160306_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='labourcost_detail',
            field=models.ManyToManyField(to='parts.LabourCost'),
        ),
    ]
