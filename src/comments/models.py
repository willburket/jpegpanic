from typing_extensions import Self
from urllib import request
from django import forms
from django.db import models


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=150)
    comment = models.TextField()
    likes = models.IntegerField(default=0)