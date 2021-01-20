from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



# Create your models here
class Posts(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

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
