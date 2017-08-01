# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0004_auto_20160416_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
