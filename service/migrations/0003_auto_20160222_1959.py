# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_service_is_serviced'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_amount', models.FloatField(default=0)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('recieved_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='labour_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='part_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='total_paid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='total_pending',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='payment',
            field=models.ManyToManyField(to='service.Payment'),
        ),
    ]
