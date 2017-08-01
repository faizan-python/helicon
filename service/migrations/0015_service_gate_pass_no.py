# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_auto_20160521_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='gate_pass_no',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
