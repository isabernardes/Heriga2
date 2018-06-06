from django.contrib import admin

# Register your models here.
from .models import Community, Story

class StoryModelAdmin(admin.ModelAdmin):
	list_display = ["user", "community", "title", "slug","content","publish","updated", "timestamp"]
	class Meta:
		model = Story

class StoryInline(admin.TabularInline):
	model = Story
	prepopulated_fields = {'slug':('title',)}

class CommunityModelAdmin(admin.ModelAdmin):
	inlines = [StoryInline]
	list_display = ["title", "slug", "timestamp"]

	class Meta:
		model = Community

admin.site.register(Community, CommunityModelAdmin)
admin.site.register(Story, StoryModelAdmin)
