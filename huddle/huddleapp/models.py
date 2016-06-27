from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    student_answer = models.CharField(max_length=500)
    instructor_answer = models.CharField(max_length=500)

class Followup(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    followup_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

class FollowupComment(models.Model):
    followup = models.ForeignKey(Followup, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
