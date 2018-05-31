from django.contrib import admin

# Register your models here.
from .models import Community

class CommunityModelAdmin(admin.ModelAdmin):
	list_display = ["title", "slug", "update","timestamp"]

	class Meta:
		model = Community

admin.site.register(Community)
