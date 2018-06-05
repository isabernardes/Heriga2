from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
	first_name = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=30,
		required=False)
	last_name = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=30,
		required=False)
	job_title = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=50,
		required=False)
	email = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=75,
		required=False)
	url = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=50,
		required=False)
	location = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		max_length=50,
		required=False)

	class Meta:
		model = Profile
		fields = ['job_title', 'url', 'location', ]

class ChangePasswordForm(forms.ModelForm):
	id = forms.CharField(widget=forms.HiddenInput())
	old_password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
		label="Old password",
		required=True)

	new_password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
		label="New password",
		required=True)
	confirm_password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
		label="Confirm new password",
		required=True)

	class Meta:
		model = User
		fields = ['id', 'old_password', 'new_password', 'confirm_password']
