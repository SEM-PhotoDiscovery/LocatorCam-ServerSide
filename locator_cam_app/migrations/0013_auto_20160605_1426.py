# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam_app', '0012_auto_20160605_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moment',
            options={'ordering': ['-pub_time_interval']},
        ),
        migrations.RemoveField(
            model_name='moment',
            name='pub_time',
        ),
        migrations.AddField(
            model_name='moment',
            name='pub_time_interval',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
    ]