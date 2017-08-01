# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0004_auto_20160307_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labourcost',
            old_name='created_by',
            new_name='created_user',
        ),
    ]
