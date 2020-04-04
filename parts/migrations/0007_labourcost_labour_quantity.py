# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0006_auto_20160307_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourcost',
            name='labour_quantity',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
