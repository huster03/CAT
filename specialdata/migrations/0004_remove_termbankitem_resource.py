# Generated by Django 5.0.4 on 2024-06-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialdata', '0003_remove_termbankitem_term_bank_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='termbankitem',
            name='resource',
        ),
    ]
