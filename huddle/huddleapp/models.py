from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
