from urllib import request
from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length=150)
    author = models.TextField(max_length=75)             # add length limit, make non-null 
    link = models.TextField(default=None, blank=True, null=True)
    likes = models.IntegerField(default = 0)
    description = models.TextField(default=None, blank=True, null=True)
    date = models.DateField(default=datetime.now)     
    source = models.TextField(default="null")   # add length limit, make non-null
    
class Comment(models.Model):
    user = models.CharField(max_length=150)
    article = models.TextField(max_length=150)    # should we do this based on article id? 
    comment = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    is_reply_to = models.IntegerField(default=None, blank=True, null=True)