from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	
	class Meta(UserCreationForm.Meta):
		model = CustomUser

		fields = ('username','email','first_name', 'last_name','password1', 'password2',)
	field_order = ['username', 'email','first_name', 'last_name','password1', 'password2',]
	
	def save(self, commit=True):
		return None

class CustomUserChangeForm(UserChangeForm):
	password = None
	first_name = forms.CharField()
	last_name = forms.CharField()
	class Meta:
		model = CustomUser
		fields = ('email', 'username', 'first_name', "last_name",'bio', "twitter_url","instagram_url","tiktok_url","youtube_url")

