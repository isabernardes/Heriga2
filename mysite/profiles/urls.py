from django.conf.urls import url
from .views import (
	profile,
	settings,
	password
	)

urlpatterns = [
	url(r'^$', settings, name='settings'),
	url(r'^password/$', password, name='settings'),
	url(r'^(?P<username>[\w.@+-]+)/$', profile, name='profile'),

	
]