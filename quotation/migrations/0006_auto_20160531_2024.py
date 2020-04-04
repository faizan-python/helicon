# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0005_quotation_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_order_number', models.CharField(max_length=50, blank=True)),
                ('total_cost', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('estimated_delivery', models.CharField(max_length=150, null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('parts', models.ManyToManyField(to='quotation.QuotationPart')),
            ],
        ),
        migrations.AddField(
            model_name='quotation',
            name='performa',
            field=models.ManyToManyField(to='quotation.Performa'),
        ),
    ]
