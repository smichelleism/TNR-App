from django import forms
from .forms import TNRApplicationModelForm
from django.shortcuts import render, redirect

# Create your views here.

def application_upload(request):
	if request.method == "POST":
		form = TNRApplicationModelForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('https://kittybungalow.org')
	else:
		form = TNRApplicationModelForm()

	return render(request, "application.html", {'form':form})