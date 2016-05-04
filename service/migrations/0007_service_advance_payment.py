# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_remove_service_advance_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='advance_payment',
            field=models.FloatField(default=0),
        ),
    ]
