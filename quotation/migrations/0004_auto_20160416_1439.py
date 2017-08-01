# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0003_quotation_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='total_price',
            new_name='total_cost',
        ),
    ]
