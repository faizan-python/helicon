# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_service_gate_pass_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='party_tin_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='purchase_order_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
