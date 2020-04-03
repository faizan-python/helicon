# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0006_auto_20160531_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='performa',
            name='tax_amount',
            field=models.FloatField(default=0),
        ),
    ]
