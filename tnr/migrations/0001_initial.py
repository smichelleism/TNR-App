# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TNRApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_status', models.CharField(choices=[('Ban', 'Banned'), ('Csd', 'Closed'), ('Ipr', 'In Progress'), ('NCt', 'New Contact'), ('Out', 'Out of Area'), ('Pnd', 'Pending'), ('STr', 'Self Trapping')], default='NCt', max_length=3)),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=100, verbose_name='What is your first name?')),
                ('last_name', models.CharField(max_length=100, verbose_name='What is your family (last) name?')),
                ('email', models.CharField(max_length=100, verbose_name='What is your email?')),
                ('contact_street_address', models.CharField(blank=True, max_length=200, verbose_name='What is your home street address?')),
                ('contact_city', models.CharField(blank=True, max_length=50, verbose_name='What is your home city?')),
                ('contact_state', models.CharField(blank=True, default='CA', max_length=2, verbose_name='What state do you live in?')),
                ('contact_zipcode', models.CharField(blank=True, max_length=10, verbose_name='What is your home zip code?')),
                ('contact_phone_cell', models.CharField(blank=True, max_length=20, verbose_name='What is your cell phone number?')),
                ('contact_phone_land', models.CharField(blank=True, max_length=20, verbose_name='What is your home telephone number?')),
                ('colony_street_address', models.CharField(blank=True, max_length=200, verbose_name='What is the street address for the colony?')),
                ('colony_cross_streets', models.CharField(blank=True, max_length=200, verbose_name='What are the major cross streets nearest the colony?')),
                ('colony_city', models.CharField(blank=True, max_length=50, verbose_name='What city is the colony located?')),
                ('colony_state', models.CharField(blank=True, default='CA', max_length=2)),
                ('colony_zipcode', models.CharField(blank=True, max_length=10, verbose_name='What is the zip code where the colony is located?')),
                ('transportation', models.CharField(blank=True, max_length=20, verbose_name='Do you have a car or other transportation to help with taking the cats to/from the vet?')),
                ('location_type', models.CharField(blank=True, max_length=10, verbose_name='Please describe the colony location. Is it a business/home/school/field/or ...')),
                ('cats_total', models.CharField(blank=True, max_length=50, verbose_name='How many cats total (including kittens)?')),
                ('kittens_total', models.CharField(blank=True, max_length=50, verbose_name='How many kittens are there? What is their approximate age?')),
                ('cats_friendly', models.CharField(blank=True, max_length=100, verbose_name='Are any of the cats friendly? Can you touch them?')),
                ('cats_pregnant', models.CharField(blank=True, max_length=100, verbose_name='Do you know if any of the cats are currently pregnant?')),
                ('cats_fixed', models.CharField(blank=True, max_length=100, verbose_name='Do you know if any of the cats are already fixed?')),
                ('cats_feeding', models.CharField(blank=True, max_length=200, verbose_name='Who feeds the cats? What time are they normally fed (morning/evening)?')),
                ('scheduling_issues', models.CharField(blank=True, max_length=200, verbose_name='The community partner needs to be present to show us where the cats hang out. Are there any scheduling issues?')),
                ('add_info', models.TextField(blank=True, verbose_name='Is there any additional information which would helpful?')),
                ('notes', models.TextField(blank=True, verbose_name='Private KB Notes about location.')),
            ],
        ),
        migrations.CreateModel(
            name='TNREvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Short Description')),
                ('desc', models.CharField(blank=True, max_length=200, verbose_name='Long Description')),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TNRLeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TNRLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_name', models.CharField(blank=True, max_length=200)),
                ('cp_email', models.CharField(blank=True, max_length=200)),
                ('cp_telephone', models.CharField(blank=True, max_length=200)),
                ('colony_address01', models.CharField(blank=True, max_length=200)),
                ('colony_address02', models.CharField(blank=True, max_length=200)),
                ('colony_city', models.CharField(blank=True, max_length=50)),
                ('colony_zipcode', models.CharField(blank=True, max_length=10)),
                ('date_sched', models.DateField(blank=True, null=True)),
                ('notes_public', models.TextField(blank=True, verbose_name='Public Notes')),
                ('notes_private', models.TextField(blank=True, verbose_name='Private Notes. (Not to be shared with CP.)')),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tnr.TNRApplication')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tnr.TNREvent')),
            ],
        ),
        migrations.CreateModel(
            name='TNRRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('leg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tnr.TNRLeg')),
            ],
        ),
        migrations.CreateModel(
            name='Trap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Itk', 'Intake'), ('Dec', 'Deceased'), ('Rel', 'Released to Colony'), ('Oth', 'Other'), ('Unk', 'Unknown')], default='Unk', max_length=3)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unknown')], default='Unk', max_length=1)),
                ('trap_no', models.CharField(max_length=20)),
                ('cat_desc', models.CharField(max_length=100)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tnr.TNRLocation')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tnr.TNRRole'),
        ),
    ]
