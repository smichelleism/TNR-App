# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0025_tnrlocation_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tnrlocation',
            name='event',
        ),
        migrations.AddField(
            model_name='tnrlocation',
            name='event',
            field=models.ManyToManyField(default=1, to='tnr.TNREvent'),
        ),
    ]
