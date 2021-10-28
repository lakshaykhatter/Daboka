from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.validators import UsernameValidator
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    bio = models.TextField(null=True,blank=True)
    twitter_url = models.URLField(max_length=300, null=True,blank=True)
    tiktok_url = models.URLField(max_length=300, null=True,blank=True)
    instagram_url = models.URLField(max_length=300, null=True,blank=True)
    youtube_url = models.URLField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=300,unique=True, null=True, validators=[UsernameValidator()])

    def __str__(self):
        return self.email