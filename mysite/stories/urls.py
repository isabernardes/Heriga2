from django.conf.urls import url
from django.urls import reverse


from .views import (
	communities_list,
	communities_create,
	communities_detail,
	stories_detail,
	communities_update,
	communities_delete,
	)

urlpatterns = [
    url(r'^$', communities_list, name="list"),
    url(r'^create/$', communities_create),
    url(r'^(?P<slug>[\w-]+)/$', communities_detail, name="detail"),
    url(r'^(?P<c_slug>[\w-]+)/(?P<s_slug>[\w-]+)/$', stories_detail, name="stories_detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', communities_update, name="updates"),
    url(r'^(?P<slug>[\w-]+)/delete/$', communities_delete),
    
]

