from django.conf.urls import url
from django.urls import reverse


from .views import (
	communities_list,
	communities_create,
	communities_detail,
	communities_update,
	communities_delete,
	stories_create,
	stories_detail,
	stories_update,
	stories_delete,
	)

urlpatterns = [
    url(r'^$', communities_list, name="communities_list"),
    url(r'^create/$', communities_create),
    url(r'^(?P<c_slug>[\w-]+)/$', communities_detail, name = 'communities_detail' ), #List of stories of each community
    url(r'^(?P<c_slug>[\w-]+)/edit/$', communities_update, name="communities_update"),
 	url(r'^(?P<c_slug>[\w-]+)/delete/$', communities_delete),
    
 	#STORIES

    url(r'^(?P<c_slug>[\w-]+)/story/create/$', stories_create),
    url(r'^(?P<c_slug>[\w-]+)/(?P<s_slug>[\w-]+)/$', stories_detail, name="stories_detail"), #Detail of a story
    url(r'^(?P<c_slug>[\w-]+)/(?P<s_slug>[\w-]+)/edit/$', stories_update, name="stories_updates"),
    url(r'^(?P<c_slug>[\w-]+)/(?P<s_slug>[\w-]+)/delete/$', stories_delete),
    
]

