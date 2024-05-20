from __future__ import unicode_literals
from django.db import models

class Specialdatatable(models.Model):
    objects = models.Manager()
    source_text = models.TextField()
    target_text = models.TextField()
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)