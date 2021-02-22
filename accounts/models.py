from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="media/images/")
    bio = models.TextField(blank=True)
    profile_background = models.ImageField(null=True, blank=True, upload_to="media/images/")