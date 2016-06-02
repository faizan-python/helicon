# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20160414_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tin_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
