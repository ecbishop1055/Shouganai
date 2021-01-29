from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



# Create your models here
class Posts(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    post_image = models.ImageField(null=True, blank=True, upload_to="media/images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Profile(models.Model):
    user = models.OneToOneField('accounts.CustomUser', null=True, on_delete=models.CASCADE)
    bio = models.TextField()
<<<<<<< HEAD
    # profile = 
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
=======
    profile_pic = models.ImageField(null=True, blank=True, upload_to="media/images/")
>>>>>>> 3904999db2e2ed01ed327e3527072cbf965d2f62
    github = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

