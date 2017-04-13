# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_auto_20170219_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_retail_invoice', models.CharField(max_length=100, null=True, blank=True)),
                ('latest_tax_invoice', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='retail_invoice_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='tax_invoice_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
