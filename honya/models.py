from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ArticleInfo(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    content = models.TextField()
    bcomment =models.IntegerField(default=0)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    bcomment =models.IntegerField(default=0)
    usertype = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.username