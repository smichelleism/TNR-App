from django import forms
from .forms import TNRApplicationModelForm
from django.shortcuts import render

# Create your views here.

def application_upload(request):
	if request.method == "POST":
		form = TNRApplicationModelForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
	else:
		form = TNRApplicationModelForm()

	return render(request, "application.html", {'form':form})