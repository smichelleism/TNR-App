# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0009_auto_20171218_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='trap',
            name='cat_age',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='trap',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]