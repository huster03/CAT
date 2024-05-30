# Generated by Django 5.0.4 on 2024-05-23 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialdata', '0001_initial'),
        ('usersignin', '0003_remove_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermBankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_bank_name', models.TextField()),
                ('source_text', models.TextField()),
                ('target_text', models.TextField()),
                ('resource', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersignin.user')),
            ],
        ),
        migrations.CreateModel(
            name='TermBankList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_language', models.TextField()),
                ('target_language', models.TextField()),
                ('term_bank', models.TextField()),
                ('number_of_terms', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersignin.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Specialdatatable',
        ),
    ]
