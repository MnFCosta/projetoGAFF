# Generated by Django 4.1.6 on 2023-03-09 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ultimo_login',
        ),
    ]