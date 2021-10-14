from django import forms
from posts.models import Post

# class CodeSearchForm(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = ['urlhash']

class CodeSearchForm(forms.Form):
    urlhash = forms.CharField(label='Code', max_length=100)
