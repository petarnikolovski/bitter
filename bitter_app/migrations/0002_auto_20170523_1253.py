# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(default='settings.MEDIA_ROOT/avatars/avatar_default.jpeg', upload_to='avatars/%Y/%m/%d'),
        ),
    ]