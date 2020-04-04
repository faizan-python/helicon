# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_auto_20160716_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='freight_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='invoice_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
