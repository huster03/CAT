# Generated by Django 5.0.4 on 2024-05-20 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersignin', '0002_texttranslationpart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]