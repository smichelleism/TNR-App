from django.contrib import admin
from .models import TNRApplication, TNRLocation, Trap


# Register your models here.

class TrapInline(admin.TabularInline):
	model = Trap


@admin.register(Trap)
class TrapAdmin(admin.ModelAdmin):
	list_display = ('trap_no', 'cat_desc', 'gender')

@admin.register(TNRLocation)
class TRNLocationAdmin(admin.ModelAdmin):
	list_display = ('cp_name', 'cp_telephone', 'cp_email', 'colony_address01', 'colony_zipcode', 'date_sched')
	list_filter = ['date_sched']
	inlines = [ TrapInline, ]

@admin.register(TNRApplication)
class TNRApplicationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Initial Application Date',
			{'fields': ['application_date']}),
		('Applicant Information',
			{'fields': ['last_name', 'first_name', 'email', 'contact_street_address', 'contact_city', 'contact_zipcode']}),
		('Colony Address',
			{'fields': ['colony_cross_streets', 'colony_street_address', 'contact_city', 'colony_zipcode']}),
		('Colony Information',
			{#'classes': ('collapse',),
			'fields': ['cats_total', 'kittens_total', 'cats_friendly', 'cats_pregnant', 'cats_fixed', 'cats_feeding', 'scheduling_issues', 'add_info']}),
		('KB Notes',
			{'fields': ['notes', 'app_status']}),
		]

	list_display = ('application_date', 'first_name', 'last_name', 'colony_street_address', 'cats_total', 'app_status')
	search_fields = ['last_name', 'colony_street_address']
	list_filter = ['application_date', 'app_status']
	