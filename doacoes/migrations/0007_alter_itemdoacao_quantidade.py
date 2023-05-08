# Generated by Django 4.1.6 on 2023-05-05 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0006_alter_doacao_data_doacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdoacao',
            name='quantidade',
            field=models.DecimalField(decimal_places=0, max_digits=20, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]