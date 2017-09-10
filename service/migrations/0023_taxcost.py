# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_service_gst_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxCost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('igst', models.FloatField(default=0)),
                ('sgst', models.FloatField(default=0)),
                ('cgst', models.FloatField(default=0)),
            ],
        ),
    ]
