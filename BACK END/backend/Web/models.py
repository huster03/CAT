from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class UserProject(models.Model):
    project_name = models.CharField(max_length=32)
    import_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

class MemoryBankList(models.Model):
    memory_bank_name = models.CharField(max_length=32)
    original_language = models.CharField(max_length=32)
    target_language = models.CharField(max_length=32)
    number_of_memory_items = models.IntegerField()

class MemoryBankItem(models.Model):
    memory_bank_name = models.CharField(max_length=32)
    memory_item_id = models.IntegerField()
    original_language_text = models.CharField(max_length=32)
    target_language_text = models.CharField(max_length=32)
    import_time = models.DateTimeField(auto_now_add=True)
    number_of_calls = models.IntegerField()

class TermBankList(models.Model):
    term_bank_name = models.CharField(max_length=32)
    original_language = models.CharField(max_length=32)
    target_language = models.CharField(max_length=32)
    number_of_term_items = models.IntegerField()

class TermBankItem(models.Model):
    term_bank_name = models.CharField(max_length=32)
    term_item_id = models.IntegerField()
    original_language_text = models.CharField(max_length=32)
    target_language_text = models.CharField(max_length=32)
    source = models.CharField(max_length=32)