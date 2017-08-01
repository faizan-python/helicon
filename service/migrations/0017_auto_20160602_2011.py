# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_auto_20160601_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='party_tin_number',
        ),
        migrations.AddField(
            model_name='service',
            name='purchase_order_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
