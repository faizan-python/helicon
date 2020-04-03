# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0008_performa_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='performa',
        ),
        migrations.AddField(
            model_name='quotation',
            name='performa',
            field=models.ForeignKey(blank=True, to='quotation.Performa', null=True),
        ),
    ]
