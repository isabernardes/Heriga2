from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["user", "location", "url","job_title"]

	class Meta:
		model = Profile

admin.site.register(Profile, ProfileModelAdmin)