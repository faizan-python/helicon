# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20160517_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cheque_number',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Cash', b'CASH'), (b'Cheque', b'CHEQUE'), (b'Others', b'OTHERS')]),
        ),
    ]
