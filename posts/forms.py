from django import forms
from posts.models import Post, Link
from crispy_forms.helper import FormHelper
from django.forms.models import BaseModelFormSet

# class PostCreateForm(forms.Form):
#     author = forms.CharField()
#     title = forms.CharField()
#     description = forms.CharField()

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields =  ['title', 'description', ]

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ["url",]