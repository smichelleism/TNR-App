from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import TNRApplication, TNRLocation, Trap, TNREvent


# Register your models here.

class TrapInline(admin.TabularInline):
	model = Trap
	formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
    }
	#extra = 0

class LocationInline(admin.StackedInline):
	model = TNRLocation
	extra = 0

class LocationInlineTab(admin.TabularInline):
	model = TNRLocation
	extra = 0

# class EventInlineTab(admin.TabularInline):
#	model = TNRLocation.events.through
#	formfield_overrides = {
#        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
#        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
#    }

@admin.register(TNREvent)
class TNREventAdmin(admin.ModelAdmin):
	list_display = ('date', 'name', 'desc')
	inlines = [ TrapInline, ]

@admin.register(Trap)
class TrapAdmin(admin.ModelAdmin):
	list_display = ('trap_no', 'cat_desc', 'gender')


@admin.register(TNRLocation)
class TRNLocationAdmin(admin.ModelAdmin):
	list_display = ('cp_name', 'cp_telephone', 'cp_email', 'colony_address01', 'colony_zipcode')
#	inlines = [ EventInlineTab, ]
	search_fields = ['cp_name', 'colony_address01']
	list_filter = ['loc_status']

@admin.register(TNRApplication)
class TNRApplicationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Initial Application Date',
			{'fields': [ 'app_status', 'outcome_status', 'application_date']}),
		('Applicant Information',
			{'fields': ['last_name', 'first_name', 'email', 'contact_phone_cell', 'contact_phone_land', 'contact_street_address', 'contact_city', 'contact_zipcode', 'occupation', 'hh_income']}),
		('Colony Address',
			{'fields': ['colony_cross_streets', 'colony_street_address', 'colony_city', 'colony_zipcode']}),
		('Colony Information',
			{#'classes': ('collapse',),
			'fields': ['cats_total', 'kittens_total', 'cats_friendly', 'cats_pregnant', 'cats_fixed', 'cats_feeding', 'location_type', 'scheduling_issues', 'add_info']}),
		('KB Notes',
			{'fields': ['notes']}),
		]

	list_display = ('application_date', 'app_status', 'outcome_status', 'first_name', 'last_name', 'email', 'contact_phone_cell', 'colony_street_address', 'cats_total')
	search_fields = ['last_name', 'first_name', 'email', 'colony_street_address']
	list_filter = ['app_status', 'outcome_status', 'application_date']
	inlines = [LocationInline, ]
	