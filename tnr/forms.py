from django import forms
from .models import TNRApplication

class TNRApplicationModelForm(forms.ModelForm):
	class Meta:
		model = TNRApplication
		fields = ('last_name', 
			'first_name', 
			'email', 
			'contact_street_address', 
			'contact_city',  
			'contact_zipcode', 
			'contact_phone_cell', 
			'contact_phone_land', 
			'colony_street_address',
			'colony_cross_streets',
			'colony_city',
			'colony_zipcode',
			'transportation',
			'location_type',
			'cats_total',
			'kittens_total',
			'cats_pregnant',
			'cats_friendly',
			'cats_fixed',
			'cats_feeding',
			'scheduling_issues',
			'add_info')
