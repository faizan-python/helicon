# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehical', '0003_auto_20160306_1452'),
        ('service', '0008_auto_20160229_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='otherservice',
            field=models.ForeignKey(blank=True, to='vehical.OtherService', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='vehical',
            field=models.ForeignKey(blank=True, to='vehical.Vehical', null=True),
        ),
    ]
