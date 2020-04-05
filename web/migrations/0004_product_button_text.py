# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='button_text',
            field=models.CharField(default=b'Buy Now', max_length=250),
        ),
    ]
