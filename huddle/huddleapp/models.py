from __future__ import unicode_literals
from rest_framework import serializers

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    student_answer = models.CharField(max_length=500)
    instructor_answer = models.CharField(max_length=500)
    def __str__(self):
        return "title:  " + self.title + "\n" + "body:   " + self.body + "\n" + "author: " + self.author + "\n"

class Followup(models.Model):
    post = models.ForeignKey(Post, related_name='followups', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    followup_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

class FollowupComment(models.Model):
    followup = models.ForeignKey(Followup, related_name='followupComments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

class FollowupCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowupComment

class FollowupSerializer(serializers.ModelSerializer):
    followupComments = FollowupCommentSerializer(many=True)
    class Meta:
        model = Followup
        fields = ('id', 'post', 'author', 'followup_text', 'pub_date',
                  'followupComments')


class PostSerializer(serializers.ModelSerializer):
    followups = FollowupSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'pub_date',
                  'student_answer', 'instructor_answer', 'followups')


