from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

#App-Status
# - New Contact
# - In Progress
# - Pending
# - Closed

#App-Outcome
# - Self-trapping
# - No action taken
# - Location closed
# - Out of Area
# - Banned



class TNRApplication(models.Model):
    INPROGRESS	= 'In Progress'
    CLOSED 		= 'Closed'
    PENDING		= 'Pending'
    NEWCONTACT	= 'New Contact'

    LEVEL24 = '24'
    LEVEL35 = '35'
    LEVEL65 = '65'
    LEVEL99 = '99'

    OUTAREA     = 'Out of Area'
    BANNED      = 'Banned'
    SELFTRAP    = 'Self-Trapping'
    NOACTION    = 'No Action'
    LOCCLOSED   = 'Location Closed'
    SCHEDULED   = 'Scheduled'
    FLYER       = 'Needs Flyering'

    HH_INCOME_CHOICES   = (
        (LEVEL24, "Below 24,000"),
        (LEVEL35, "Between 24,000 and 35,000"),
        (LEVEL65, "Between 35,000 and 65,000"),
        (LEVEL99, "Above 65,000"),
        )

    APP_STATUS_CHOICES	= (
		(CLOSED, "Closed"),
		(INPROGRESS, "In Progress"),
		(NEWCONTACT, "New Contact"),
		(PENDING, "Pending"),
		)

    OUTCOME_STATUS_CHOICES  = (
        (BANNED, "Banned"),
        (NOACTION, "Closed-No Action"),
        (LOCCLOSED, "Location Closed"),
        (OUTAREA, "Out of Area"),
        (SELFTRAP, "Self Trapping"),
        (SCHEDULED, 'Scheduled'),
        (FLYER, 'Needs Flyering'),
        )

    app_status 				= models.CharField(max_length = 15, choices=APP_STATUS_CHOICES, default=NEWCONTACT)
    outcome_status          = models.CharField(max_length = 20, choices=OUTCOME_STATUS_CHOICES, blank=True, null=True)
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
        blank=True, null=True)
    contact_city            = models.CharField(
        verbose_name='What is your home city?', 
        max_length=50,  
        blank=True, null=True)
    contact_state           = models.CharField(
        verbose_name='What state do you live in?',
        max_length=2, 
        default="CA", 
        blank=True, null=True)
    contact_zipcode         = models.CharField(
        verbose_name='What is your home zip code?', 
        max_length=10, 
        blank=True, null=True)
    occupation              = models.CharField(
        verbose_name='What is your occupation?', 
        max_length=100, 
        blank=True, null=True)
    hh_income               = models.CharField(
        verbose_name='What is your household income?',
        max_length = 2, 
        choices=HH_INCOME_CHOICES, 
        blank=True, null=True)
    contact_phone_cell		= models.CharField(
        verbose_name='What is your cell phone number?', 
        max_length=20, 
        blank=True, null=True)
    contact_phone_land		= models.CharField(
        verbose_name='What is your home telephone number?', 
        max_length=20, 
        blank=True, null=True)
    colony_street_address   = models.CharField(
        verbose_name='What is the street address for the colony?', 
        max_length=200, 
        blank=True, null=True)
    colony_cross_streets    = models.CharField(
        "What are the major cross streets nearest the colony?",
        max_length=200, 
        blank=True, null=True)
    colony_city             = models.CharField(
        verbose_name='What city is the colony located?', 
        max_length=50,  
        blank=True, null=True)
    colony_state            = models.CharField(
        max_length=2, 
        default="CA", 
        blank=True, null=True)
    colony_zipcode          = models.CharField(
        verbose_name='What is the zip code where the colony is located?', 
        max_length=10, 
        blank=True, null=True)
    transportation          = models.CharField(
        verbose_name='Do you have a car or other transportation to help with taking the cats to/from the vet?', 
        max_length=20,
        blank=True, null=True)
    location_type           = models.CharField(
        verbose_name='Please describe the colony location. Is it a business/home/school/field/or ...', 
        max_length=100, 
        blank=True, null=True)
    cats_total              = models.CharField(
        verbose_name='How many cats total (including kittens)?', 
        max_length=50, 
        blank=True, null=True)
    kittens_total           = models.CharField(
        verbose_name='How many kittens are there? What is their approximate age?', 
        max_length=50, 
        blank=True, null=True)
    cats_friendly           = models.CharField(
        verbose_name='Are any of the cats friendly? Can you touch them?', 
        max_length=100, 
        blank=True, null=True)
    cats_pregnant           = models.CharField(
        verbose_name='Do you know if any of the cats are currently pregnant?', 
        max_length=100, 
        blank=True, null=True)
    cats_fixed              = models.CharField(
        verbose_name='Do you know if any of the cats are already fixed?', 
        max_length=100, 
        blank=True, null=True)
    cats_feeding            = models.CharField(
        verbose_name='Who feeds the cats? What time are they normally fed? Morning/evening? What time?', 
        max_length=200, 
        blank=True, null=True)
    scheduling_issues       = models.CharField(
        verbose_name='The community partner needs to be present to show us where the cats hang out. Are there any scheduling issues?', 
        max_length=200, 
        blank=True, null=True)
    add_info                = models.TextField(
        verbose_name='Is there any additional information which would helpful?', 
        blank=True, null=True)
    notes                   = models.TextField(
        verbose_name='Private KB Notes about location.', 
        blank=True, null=True)


    def __str__(self):
        return self.last_name + ', ' + self.first_name



class TNRLocation(models.Model):
    OPEN        = 'O'
    CLOSED      = 'C'

    LOC_STATUS_CHOICES  = (
        (OPEN, "Open"),
        (CLOSED, "Closed"),
        )

    loc_status          = models.CharField(max_length = 1, choices=LOC_STATUS_CHOICES, default=OPEN)
    cp_name             = models.CharField(max_length=200, blank=True, null=True)
    cp_email            = models.CharField(max_length=200, blank=True, null=True)
    cp_telephone        = models.CharField(max_length=200, blank=True, null=True)
    colony_address01    = models.CharField(max_length=200, blank=True, null=True)
    colony_address02    = models.CharField(max_length=200, blank=True, null=True)
    colony_city         = models.CharField(max_length=50, blank=True, null=True)
    colony_zipcode      = models.CharField(max_length=10, blank=True, null=True)
    notes_public        = models.TextField("Public Notes", blank=True, null=True)
    application	 		= models.ForeignKey(TNRApplication, blank=True, null=True)  

    def __str__(self):
    	return self.cp_name + "/" + (str)(self.colony_address01)

    class Meta:
        ordering = ('cp_name',)



class TNREvent(models.Model):
    name = models.CharField("Short Description", max_length=50, blank=True, null=True)
    desc = models.CharField("Long Description", max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
#    location = models.ManyToManyField(TNRLocation, blank=True, related_name="events")

    def __str__(self):
        return (str)(self.date) + " / " + self.name

    class Meta:
        ordering = ('name',)



class Trap(models.Model):
    FEMALE 	= 'F'
    MALE 	= 'M'
    UNKNOWN = 'U'

    GENDER_CHOICES = (
		(FEMALE, "Female"),
		(MALE, "Male"),
		(UNKNOWN, 'Unknown'),
		)

    INTAKE = 'I'
    RELEASED = 'R'
    DECEASED = 'D'
    UNKNOWN = 'U'
    OTHER = 'O'
    HOMESCHOOL = 'H'

    STATUS_CHOICES = (
        (INTAKE, 'Intake'),
        (HOMESCHOOL, 'Homeschool'),
        (DECEASED, 'Deceased' ),
        (RELEASED, 'Released to Colony'),
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
        )

    location =  models.CharField(max_length=50, blank=True, null=True) 
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=UNKNOWN, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNKNOWN, blank=True, null=True )
    trap_no	= models.CharField(max_length=20, blank=True, null=True )
    cat_desc = models.CharField(max_length=100, blank=True, null=True )
    cat_age =   models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    event = models.ForeignKey(TNREvent, blank=True, null=True, )



class TNRLeg(models.Model):
    name        = models.CharField(max_length=50, blank=True, null=True)
    date        = models.DateTimeField(blank=True, null=True)



class TNRRole(models.Model):
    leg   = models.ForeignKey(TNRLeg, on_delete=models.CASCADE, blank=True, null=True)
    name  = models.CharField(max_length=50, blank=True, null=True)



class Person(models.Model):
    role       = models.ForeignKey(TNRRole, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name  = models.CharField(max_length=100, blank=True, null=True)
    email      = models.CharField(max_length=200, blank=True, null=True)