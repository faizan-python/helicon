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
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_name', models.CharField(max_length=50, blank=True)),
                ('part_company_name', models.CharField(max_length=50, blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('part_quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
