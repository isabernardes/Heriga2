from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Comment


def comment_delete(request, id):
    obj = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        #messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(parent_obj_url)
    context = {
        "object": obj
    }
    return render(request, "confirm_delete.html", context)