# Generated by Django 4.1.6 on 2023-03-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, unique=True),
        ),
    ]
