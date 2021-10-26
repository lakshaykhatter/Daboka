from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
import string 
import random 



class Post(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title = models.CharField(max_length = 500)
	description = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	urlhash = models.CharField(max_length=7, null=True, blank=False, unique=True)
	


	def get_link_children(self):
		return self.links.all()

	def __str__(self): 
		return self.title
	
	def save(self):
		def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
			return ''.join(random.choice(chars) for _ in range(size))
			
		if not self.urlhash:
			# Generate ID once, then check the db. If exists, keep trying.
			self.urlhash = id_generator()
			while Post.objects.filter(urlhash=self.urlhash).exists():
				self.urlhash = id_generator()
		super(Post, self).save()


class Link(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='links')
	url = models.CharField(max_length=1000)
	

	def __str__(self):
		return self.url