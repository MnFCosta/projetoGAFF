# Generated by Django 3.2.9 on 2023-04-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0005_alter_doacao_data_doacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='data_doacao',
            field=models.DateField(default=None),
        ),
    ]