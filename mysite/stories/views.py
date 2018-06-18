from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Community, Story
from .forms import CommunityForm, StoryForm

# Create your views here.

def communities_create(request):
	form = CommunityForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user=request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form

	}
	return render(request, "communities_form.html", context)

def communities_list(request):
	communities = Community.objects.all()
	context = {
		"object_list":communities,
		"title":"List"
	}
	return render(request, "communities_list.html", context)


def communities_detail(request, c_slug=None): #retrieve
	instance = get_object_or_404(Community, slug=c_slug)
	context = {
		"title": instance.title,
		"instance":instance,
	}
	return render(request, "communities_detail.html", context)


def communities_update(request, c_slug=None):
	instance = get_object_or_404(Community, slug=c_slug)
	form = CommunityForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user=request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		"title": instance.title,
		"instance":instance,
		"form":form
	}
	return render(request, "communities_form.html", context)




def communities_delete(request, c_slug = None):
	instance = get_object_or_404(Community, slug=c_slug)
	instance.delete()
	return redirect('communities:list') 


#STORIES

def stories_create(request, c_slug):
	try:
		stories = Story.objects.get(community__slug=c_slug)
	except Exception:
		stories = None 
	community_id = Community.objects.get(slug=c_slug)
	form = StoryForm(request.POST or None, initial={'community': community_id.pk  })
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user=request.user
		instance.save()
		form.save_m2m()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form,
		"stories":stories,

	}
	return render(request, "stories_form.html", context)


def stories_detail(request, c_slug, s_slug): # post = Post.objects.get(<name_of_field>=<argument_in_url>)
	instance = Story.objects.all()
	stories = get_object_or_404(Story, community__slug=c_slug, slug = s_slug)

	context = {
		"stories":stories,
		"instance":instance,
	}
	return render(request, "stories_detail.html", context)

def stories_update(request, c_slug = None, s_slug =None):
	instance = get_object_or_404(Story, community__slug=c_slug, slug=s_slug)
	form = StoryForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user=request.user
		instance.save()
	context = {
		"instance":instance,
		"form":form
	}
	return render(request, "stories_form.html", context)

def stories_delete(request, c_slug = None, s_slug = None):
	instance = get_object_or_404(Story, community__slug = c_slug, slug=s_slug)
	instance.delete()
	return redirect('communities:list')

def tags(request, tag):
	stories = Story.objects.filter(tags__name=tag)
	context={
            'stories': stories,
            'tag':tag,
        } 
 
	return render(request, "tags_list.html", context)


