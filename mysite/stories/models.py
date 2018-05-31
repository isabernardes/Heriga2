from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Community (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('communities:detail', kwargs = {'slug': self.slug})

    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Communities"



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Community.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_community_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_community_receiver, sender=Community)





















'''
class Story (models.Model) 
user = models.ForeignKey(settings.AUTH_USER_MODEL, default =1)
communities = 
title = models.CharField(max_length=120)
slug = models.SlugField(unique=True)
image = models.ImageField(upload_to=upload_location, 
        null=True, 
        blank=True, 
        width_field="width_field", 
        height_field="height_field")
content = models.TextField(null=True, blank = False)
draft = models.BooleanField(default=False)
publish = models.DateField(auto_now=False, auto_now_add=False)
updated = models.DateTimeField(auto_now=True, auto_now_add=False)
timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

'''