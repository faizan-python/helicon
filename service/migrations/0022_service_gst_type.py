# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_auto_20170414_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='gst_type',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
