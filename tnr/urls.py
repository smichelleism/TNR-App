from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.application_upload, name='index'),
]