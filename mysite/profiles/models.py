from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from django.contrib.auth import user_logged_in, user_logged_out

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=50, null=True, blank=True)
	url = models.CharField(max_length=50, null=True, blank=True)
	job_title = models.CharField(max_length=50, null=True, blank=True)

	
	def __str__(self):
		return self.user.username

	def get_url(self):
		url = self.url
		if "http://" not in self.url and "https://" not in self.url and len(self.url) > 0:  
			url = "http://" + str(self.url)
		return url

	def get_screen_name(self):
		try:
			if self.user.get_full_name():
				return self.user.get_full_name()
			else:
				return self.user.username
		
		except Exception:  
			return self.user.username


	class Meta:
		verbose_name = "Profile"
		verbose_name_plural = "Profiles"

def post_save_user_model_receiver(sender,instance,created, *args, **kwargs):
	if created:
		try:
			Profile.objects.create(user=instance)
		except:
			pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
