# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='speaker',
            name='twitter',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
