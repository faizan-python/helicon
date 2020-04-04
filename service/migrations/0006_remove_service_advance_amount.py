# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_service_advance_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='advance_amount',
        ),
    ]
