from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["user", "location", "url","jobtitle"]

	class Meta:
		model = Profile

admin.site.register(Profile)