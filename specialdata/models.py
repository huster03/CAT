from __future__ import unicode_literals
from django.db import models

class TermBankList(models.Model):
    objects = models.Manager()
    source_language = models.TextField()
    target_language = models.TextField()
    term_bank = models.TextField()
    number_of_terms = models.IntegerField(default = 0)
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)

class TermBankItem(models.Model):
    objects = models.Manager()
    source_text = models.TextField()
    target_text = models.TextField()
    term_bank = models.ForeignKey('TermBankList', on_delete=models.CASCADE , default = 1)
    user = models.ForeignKey('usersignin.User', on_delete=models.CASCADE)