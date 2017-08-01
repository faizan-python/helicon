# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20160521_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cheque_bank_name',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cheque_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cheque_number',
            field=models.CharField(max_length=70, null=True, blank=True),
        ),
    ]
