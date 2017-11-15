from django import forms
from .forms import TNRApplicationForm
from django.shortcuts import render

# Create your views here.

def application_upload(request):
	if request.method == "POST":
		form = TNRApplicationForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
	else:
		form = TNRApplicationForm()

	return render(request, "application.html", {'form':form})