from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class TNREvent(models.Model):
    name = models.CharField("Short Description", max_length=50, blank=True)
    desc = models.CharField("Long Description", max_length=200, blank=True)
    date = models.DateField(blank=True)







class TNRLocation(models.Model):
    cp_name             = models.CharField(max_length=200, blank=True)
    cp_email            = models.CharField(max_length=200, blank=True)
    cp_telephone        = models.CharField(max_length=200, blank=True)
    colony_address01    = models.CharField(max_length=200, blank=True)
    colony_address02    = models.CharField(max_length=200, blank=True)
    colony_city         = models.CharField(max_length=50, blank=True)
    colony_zipcode      = models.CharField(max_length=10, blank=True)
    date_sched			= models.DateField(blank =True, default='2000-01-01')
    notes_public        = models.TextField("Public Notes", blank=True)
    notes_private       = models.TextField("Private Notes. (Not to be shared with CP.)", blank=True)



class Trap(models.Model):
	FEMALE 	= 'F'
	MALE 	= 'M'
	UNKNOWN = 'U'

	GENDER_CHOICES = (
		(FEMALE, "Female"),
		(MALE, "Male"),
		(UNKNOWN, 'Unknown')
		)

	INTAKE = 'I'
	RELEASED = 'R'
	DECEASED = 'D'
	UNKNOWN = 'U'
	OTHER = 'O'

	STATUS_CHOICES = (
		(INTAKE, 'Intake'),
		(DECEASED, 'Deceased' ),
		(RELEASED, 'Released to Colony'),
		(OTHER, 'Other'),
		(UNKNOWN, 'Unknown')
		)

	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=UNKNOWN)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNKNOWN)
	trap_no	= models.CharField(max_length=20)
	cat_desc = models.CharField(max_length=100)
	location = models.ForeignKey(TNRLocation, on_delete=models.CASCADE, default=1)





class TNRLeg(models.Model):
    location    = models.ForeignKey(TNRLocation, on_delete=models.CASCADE)
    name        = models.CharField(max_length=50, blank=True)
    date        = models.DateTimeField(blank=True)



class TNRRole(models.Model):
    leg   = models.ForeignKey(TNRLeg, on_delete=models.CASCADE)
    name  = models.CharField(max_length=50, blank=True)



class Person(models.Model):
    role       = models.ForeignKey(TNRRole)
    first_name = models.CharField(max_length=100, blank=True)
    last_name  = models.CharField(max_length=100, blank=True)
    email      = models.CharField(max_length=200, blank=True)


class TNRApplication(models.Model):
	BANNED 		= 'B'
	INPROGRESS	= 'I'
	OUTAREA		= 'O'
	CLOSED 		= 'C'
	SELFTRAP 	= 'S'
	PENDING		= 'P'
	NEWCONTACT	= 'N'

	APP_STATUS_CHOICES	= (
		(BANNED, "Banned"),
		(CLOSED, "Closed"),
		(INPROGRESS, "In Progress"),
		(NEWCONTACT, "New Contact"),
		(OUTAREA, "Out of Area"),
		(PENDING, "Pending"),
		(SELFTRAP, "Self Trapping"),
		)

	app_status 				= models.CharField(max_length = 1, choices=APP_STATUS_CHOICES, default=NEWCONTACT)
	application_date		= models.DateTimeField(default=timezone.now)
	first_name              = models.CharField(
        verbose_name='What is your first name?', 
        max_length=100)
	last_name               = models.CharField(
        verbose_name='What is your family (last) name?', 
        max_length=100)
	email                   = models.CharField(
        verbose_name='What is your email?', 
        max_length=100)
	contact_street_address  = models.CharField(
        verbose_name='What is your home street address?', 
        max_length=200, 
        blank=True)
	contact_city            = models.CharField(
        verbose_name='What is your home city?', 
        max_length=50, default="Los Angeles", 
        blank=True)
	contact_state           = models.CharField(
        verbose_name='What state do you live in?',
        max_length=2, 
        default="CA", 
        blank=True)
	contact_zipcode         = models.CharField(
        verbose_name='What is your home zip code?', 
        max_length=10, 
        blank=True)
	contact_phone_cell		= models.CharField(
        verbose_name='What is your cell phone number?', 
        max_length=20, 
        blank=True)
	contact_phone_land		= models.CharField(
        verbose_name='What is your home telephone number?', 
        max_length=20, 
        blank=True)
	colony_street_address   = models.CharField(
        verbose_name='What is the street address for the colony?', 
        max_length=200, 
        blank=True)
	colony_cross_streets    = models.CharField(
        "What are the major cross streets nearest the colony?",
        max_length=200, 
        blank=True)
	colony_city             = models.CharField(
        verbose_name='What city is the colony located?', 
        max_length=50, 
        default="Los Angeles", 
        blank=True)
	colony_state            = models.CharField(
        max_length=2, 
        default="CA", 
        blank=True)
	colony_zipcode          = models.CharField(
        verbose_name='What is the zip code where the colony is located?', 
        max_length=10, 
        blank=True)
	transportation          = models.CharField(
        verbose_name='Do you have a car or other transportation to help with taking the cats to/from the vet?', 
        max_length=20,
        blank=True)
	location_type           = models.CharField(
        verbose_name='Please describe the colony location. Is it a business/home/school/field/or ...', 
        max_length=10, 
        blank=True)
	cats_total              = models.CharField(
        verbose_name='How many cats total (including kittens)?', 
        max_length=50, 
        blank=True)
	kittens_total           = models.CharField(
        verbose_name='How many kittens are there? What is their approximate age?', 
        max_length=50, 
        blank=True)
	cats_friendly           = models.CharField(
        verbose_name='Are any of the cats friendly? Can you touch them?', 
        max_length=100, 
        blank=True)
	cats_pregnant           = models.CharField(
        verbose_name='Do you know if any of the cats are currently pregnant?', 
        max_length=100, 
        blank=True)
	cats_fixed              = models.CharField(
        verbose_name='Do you know if any of the cats are already fixed?', 
        max_length=100, 
        blank=True)
	cats_feeding            = models.CharField(
        verbose_name='Who feeds the cats? What time are they normall fed (morning/evening)?', 
        max_length=200, 
        blank=True)
	scheduling_issues       = models.CharField(
        verbose_name='The community partner needs to be present to show us where the cats hang out. Any scheduling issues which might cause issues?', 
        max_length=200, 
        blank=True)
	add_info                = models.TextField(
        verbose_name='Is there any additional information which would helpful?', 
        blank=True)
	notes                   = models.TextField(
        verbose_name='Private KB Notes about location.', 
        blank=True)
	location_sched 			= models.ForeignKey(TNRLocation, default='2000-01-01',
		verbose_name='When was this application scheduled for TNR',
		blank=True)