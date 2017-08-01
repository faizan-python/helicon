# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_service_labourcost_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_tax',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='service_tax_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='tax_amount',
            field=models.FloatField(default=0),
        ),
    ]
