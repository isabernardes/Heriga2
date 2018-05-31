from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Community
from .forms import CommunityForm

# Create your views here.

def communities_create(request):
	form = CommunityForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user=request.user
		instance.save()
		messages.sucess(request, "A new comunity was created")
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


def communities_detail(request, slug=None): #retrieve
	instance = get_object_or_404(Community, slug=slug)
	context = {
		"title": instance.title,
		"instance":instance,
	}
	return render(request, "communities_detail.html", context)

def communities_update(request, slug = None):
	instance = get_object_or_404(Community, slug=slug)
	form = CommunityForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user=request.user
		instance.save()
	messages.sucess(request, "A new comunity was created")
	return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance":instance,
		"form":form
	}
	return render(request, "communities_form.html", context)


def communities_delete(request, slug = None):
	instance = get_object_or_404(Community, slug=slug)
	instance.delete()
	return redirect('communities:list') 


