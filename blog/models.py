from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title
