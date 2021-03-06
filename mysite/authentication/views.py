from django.shortcuts import render, Http404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, ContactForm
#from stories.models import Communities


def home(request):
    title = 'Sign up now'
    form = UserRegistrationForm(request.POST or None)
    context = {
        "title": title,
        "form":form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        username = form.cleaned_data.get("username")
        if not username:
            username = "New username"
        instance.username = username
        instance.save()
        context = {
            "title": "Thank you"
        }
        return render(request, "home.html", context)


def contactus(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@email.com']
        contact_message = "%s: %s via %s"%( 
                form_full_name, 
                form_message, 
                form_email)
        some_html_message = """
        <h1>hello</h1>
        """
        send_mail(subject, 
                contact_message, 
                from_email, 
                to_email, 
                html_message=some_html_message,
                fail_silently=True)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }

    return render (request, "contactus.html")

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
            email = form.cleaned_data['email'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
        }
    return render(request, 'signup.html', context)
 
def register_success(request):
    return render_to_response('success.html')
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response('home.html',{ 'user': request.user })