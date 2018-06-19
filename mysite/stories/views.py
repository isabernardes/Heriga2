from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from django.views.decorators.http import require_POST

from .models import Community, Story
from comments.models import Comment
from comments.forms import CommentForm

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
	instance = get_object_or_404(Story, community__slug=c_slug, slug = s_slug)

	initial_data = {
		"content_type":instance.get_content_type,
		"object_id":instance.id
	}

	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = instance.get_content_type
		content_type = c_type
		
		#why doesn't content_type = ContentType.objects.get(model=c_type).model_class() work?
		#related_to_stories = Story.objects.filter(content_type=ctype)
		obj_id = form.cleaned_data.get("object_id")
		content_data = form.cleaned_data.get("content")
		
		parent_o = form.cleaned_data.get("parent")
		parent_od = form.cleaned_data.get("parent_id")
		print(parent_o)
		print(form.cleaned_data)
		print(parent_od)
		
		
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None
			print(parent_id)

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()
				print(parent_id)
				print(parent_obj)
				print(parent_qs)


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)

		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
	comments = instance.comments


	context = {
		"instance":instance,
		"comments":comments,
		"comment_form":form,


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


