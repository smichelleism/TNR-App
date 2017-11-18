# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0021_auto_20171116_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tnrlocation',
            name='trap_no',
        ),
        migrations.AddField(
            model_name='trap',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tnr.TNRLocation'),
        ),
    ]