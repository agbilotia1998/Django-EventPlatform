# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20161010_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hint1',
            field=models.CharField(default='No Hints', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='hint2',
            field=models.CharField(default='No Hints', max_length=100),
        ),
    ]
