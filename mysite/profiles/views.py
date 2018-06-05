
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404,redirect

from stories.models import Community
from .forms import ProfileForm, ChangePasswordForm





# Create your views here.
@login_required
def profile(request, username):
    page_user = get_object_or_404(User, username=username)
    communities = Community.objects.filter(user=page_user)
    communities_count = Community.objects.filter(user=page_user).count()
   
    context = {
    	'page_user':page_user,
        'communities':communities, 
        'communities_count': communities_count,   
        }

    return render(request, 'profile.html', context)

@login_required
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your profile was successfully edited.')
            return redirect ('/')

    else:
        form = ProfileForm(instance=user, initial={
            'job_title': user.profile.job_title,
            'url': user.profile.url,
            'location': user.profile.location
            })

    context = {
        'form': form
    }

    return render(request, 'settings.html', context)


@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('/')

    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form
    }   

    return render(request, 'password.html', context)




