from __future__ import unicode_literals
from django.db import models

class MemoryBankDetail(models.Model):
    objects = models.Manager()
    source_text = models.TextField()
    target_text = models.TextField()
    memory_bank = models.ForeignKey('MemoryBankList', on_delete=models.CASCADE)
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)


class MemoryBankList(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255)
    source_language = models.CharField(max_length=255)
    target_language = models.CharField(max_length=255)
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)

