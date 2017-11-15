from django import forms
from .models import TNRApplication

class TNRApplicationForm(forms.ModelForm):
	class Meta:
		model = TNRApplication
		fields = ('last_name', 'first_name', 'email')
