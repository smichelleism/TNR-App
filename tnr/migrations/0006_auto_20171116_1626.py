# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tnr', '0005_auto_20171115_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unknown')], default='U', max_length=1)),
                ('trap_no', models.CharField(max_length=5)),
                ('cat_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='tnrlocation',
            name='event',
        ),
        migrations.AlterField(
            model_name='tnrapplication',
            name='app_status',
            field=models.CharField(choices=[('B', 'Banned'), ('C', 'Closed'), ('I', 'In Progress'), ('N', 'New Contact'), ('O', 'Out of Area'), ('P', 'Pending'), ('S', 'Self Trapping')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='trap',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tnr.TNRLocation'),
        ),
    ]
