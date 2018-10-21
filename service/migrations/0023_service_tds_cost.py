# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_service_gst_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='tds_cost',
            field=models.FloatField(default=0),
        ),
    ]
