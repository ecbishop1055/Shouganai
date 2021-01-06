from django.db import models
from django.urls import reverse



# Create your models here.
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