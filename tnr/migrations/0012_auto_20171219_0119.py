# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0011_auto_20171219_0117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tnrlocation',
            options={'ordering': ('cp_name',)},
        ),
    ]