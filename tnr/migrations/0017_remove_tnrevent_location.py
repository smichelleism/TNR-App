# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-10 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0016_auto_20180621_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tnrevent',
            name='location',
        ),
    ]
