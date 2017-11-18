# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0022_auto_20171116_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='trap',
            name='status',
            field=models.CharField(choices=[('I', 'Intake'), ('D', 'Deceased'), ('R', 'Released to Colony'), ('O', 'Other'), ('U', 'Unknown')], default='U', max_length=1),
        ),
    ]