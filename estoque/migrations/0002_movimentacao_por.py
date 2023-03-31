# Generated by Django 4.1.6 on 2023-03-22 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Técnico Movimentação'),
        ),
    ]
