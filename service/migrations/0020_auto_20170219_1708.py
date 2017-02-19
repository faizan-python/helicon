# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_auto_20170219_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='challan_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='challan_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
