from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

class User(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class TextTranslationPart(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=100)
    part_index = models.IntegerField()
    source_text = models.TextField()
    target_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)