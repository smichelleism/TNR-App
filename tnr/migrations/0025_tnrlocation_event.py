# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0024_auto_20171117_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='tnrlocation',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tnr.TNREvent'),
        ),
    ]