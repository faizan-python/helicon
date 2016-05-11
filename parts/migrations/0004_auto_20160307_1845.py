# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_labourcost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labourcost',
            old_name='name',
            new_name='labour_name',
        ),
        migrations.RenameField(
            model_name='labourcost',
            old_name='price',
            new_name='labour_price',
        ),
    ]
