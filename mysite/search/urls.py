from django.conf.urls import url
from django.urls import reverse


from .views import (
	search
	)

urlpatterns = [
    url(r'^$', search, name='search'),
    #url(r'^autocomplete/',search_views.get_autocomplete_suggestions, name='autocomplete'),
]

