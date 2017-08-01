# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('gender', models.CharField(max_length=20, null=True, blank=True)),
                ('phone_number', models.IntegerField()),
                ('advance_taken', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_icon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_thumbnail', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_macroicon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
