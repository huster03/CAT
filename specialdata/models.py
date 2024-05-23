from __future__ import unicode_literals
from django.db import models

class TermBankList(models.Model):
    objects = models.Manager()
    source_language = models.TextField()
    target_language = models.TextField()
    term_bank = models.TextField()
    number_of_terms = models.IntegerField()
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)

class TermBankDetail(models.Model):
    term_bank_name = models.TextField()
    source_text = models.TextField()
    target_text = models.TextField()
    resource = models.TextField()
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)