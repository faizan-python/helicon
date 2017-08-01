# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_name', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=50, blank=True)),
                ('total_price', models.FloatField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('tax_amount', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuotationPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_name', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('part_company_name', models.CharField(max_length=50, blank=True)),
                ('price', models.FloatField(default=0)),
                ('part_quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='quotation',
            name='parts',
            field=models.ManyToManyField(to='quotation.QuotationPart'),
        ),
    ]
