from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username','email','first_name', 'last_name','password1', 'password2',)
	field_order = ['username', 'email','first_name', 'last_name','password1', 'password2',]
	
	def save(self, commit=True):
		return None

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('email', 'username', 'first_name', "last_name")

# class SignupForm(forms.Form):
# 	first_name = forms.CharField(max_length=30, label='First name')
# 	last_name = forms.CharField(max_length=30, label='last name')

# 	def signup(self, request, user):
# 		user.first_name = self.cleaned_data['first_name']
# 		user.last_name = self.cleaned_data['last_name']
# 		user.save()