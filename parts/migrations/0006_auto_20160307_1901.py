# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_auto_20160307_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labourcost',
            old_name='created_user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='labourcost',
            old_name='labour_name',
            new_name='name',
        ),
    ]
