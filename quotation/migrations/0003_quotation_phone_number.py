# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0002_auto_20160416_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='phone_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
