from django import forms
from django.core.mail import send_mail
from .forms import TNRApplicationModelForm
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@xframe_options_exempt
def application_upload(request):
	if request.method == "POST":
		form = TNRApplicationModelForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			send_mail('<test subject>', '<Hello World>', 'truancy@kittybungalow.org', ['parallaxplace@gmail.com'])
			return redirect('https://www.kittybungalow.org/tnr-application-thank-you')
	else:
		form = TNRApplicationModelForm()

	return render(request, "application.html", {'form':form})