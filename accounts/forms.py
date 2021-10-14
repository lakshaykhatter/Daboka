from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('email', 'username', 'first_name', 'last_name',)
	field_order = ['username', 'email','first_name', 'last_name','password1', 'password2',]


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('email', 'username', 'first_name', "last_name")