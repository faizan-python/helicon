# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
        ('vehical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_number', models.CharField(unique=True, max_length=50)),
                ('part_name', models.CharField(max_length=50, blank=True)),
                ('company_name', models.CharField(max_length=50, blank=True)),
                ('about', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
        ),
    ]
