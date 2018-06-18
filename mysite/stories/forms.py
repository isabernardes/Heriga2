from django import forms
from .models import Community, Story

class CommunityForm(forms.ModelForm):
	class Meta:
		model=Community
		fields = [
			"title",
			"description"
		] 

class StoryForm(forms.ModelForm):
	class Meta:
		model=Story
		fields = [
			"title",
			"content",
			#"slug",
			"community",
			"publish",
			"tags",
		] 