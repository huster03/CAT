from __future__ import unicode_literals
from django.db import models

class MemoryBankDetail(models.Model):
    objects = models.Manager()
    source_text = models.TextField()
    target_text = models.TextField()
    memory_bank = models.ForeignKey('MemoryBankList', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    called_count = models.IntegerField(default=0)
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.source_text[:100]

class MemoryBankList(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255)
    source_language = models.CharField(max_length=255)
    target_language = models.CharField(max_length=255)
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
