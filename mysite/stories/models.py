from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Community (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('communities:communities_detail', kwargs = {'c_slug': self.slug})

    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Communities"


class Story (models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    community = models.ForeignKey(Community)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(null=True, blank = False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def get_absolute_url(self):
        return reverse ('communities:stories_detail', kwargs = {'c_slug': self.community.slug, 's_slug': self.slug})

    class Meta:
        unique_together = (('slug', 'community'))

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"


#For stories
def create_slug(instance, new_slug=None): #for stories
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Story.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


#For communities
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
#pre_save.connect(pre_save_community_receiver, sender=Story)

