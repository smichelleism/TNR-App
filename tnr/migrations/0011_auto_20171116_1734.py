# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0010_auto_20171116_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnrlocation',
            name='date_sched',
            field=models.DateField(blank=True, default='2000-1-1'),
        ),
    ]