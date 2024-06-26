# Generated by Django 5.0.4 on 2024-05-15 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersignin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextTranslationPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('part_index', models.IntegerField()),
                ('source_text', models.TextField()),
                ('target_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
