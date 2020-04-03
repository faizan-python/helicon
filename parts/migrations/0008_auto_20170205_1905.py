# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_labourcost_labour_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourcost',
            name='name',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_company_name',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_name',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
