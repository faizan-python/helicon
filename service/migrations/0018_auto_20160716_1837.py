# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_auto_20160602_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehical_number', models.CharField(max_length=70, null=True, blank=True)),
                ('remark', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Advance', b'Advance'), (b'Cash', b'CASH'), (b'Cheque', b'CHEQUE'), (b'Others', b'OTHERS')]),
        ),
        migrations.AddField(
            model_name='service',
            name='delivery_invoice_details',
            field=models.ForeignKey(blank=True, to='service.DeliveryDetail', null=True),
        ),
    ]
