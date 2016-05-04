# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_service_advance_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='total_cost',
            field=models.FloatField(default=0),
        ),
    ]
