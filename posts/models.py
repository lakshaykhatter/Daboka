from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser


class Post(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title = models.CharField(max_length = 500)
	description = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self): 
		return self.title


class Link(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
	url = models.URLField()
	

	def __str__(self):
		return self.url




