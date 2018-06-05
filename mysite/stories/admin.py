from django.contrib import admin

# Register your models here.
from .models import Community, Story

class StoryInline(admin.TabularInline):
	model = Story
	prepopulated_fields = {'slug':('title',)}

class CommunityModelAdmin(admin.ModelAdmin):
	inlines = [StoryInline]
	list_display = ["title", "slug", "timestamp"]

	class Meta:
		model = Community

admin.site.register(Community, CommunityModelAdmin)
