from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import (
	home,
	contactus,
	register,
	register_success,
	logout_page,
	)

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^signups/$', register, name='signup'),
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^accounts/login/$',auth_views.login, name='login'), # If user is not login it will redirect to login page
    url(r'^register/success/$', register_success),
]