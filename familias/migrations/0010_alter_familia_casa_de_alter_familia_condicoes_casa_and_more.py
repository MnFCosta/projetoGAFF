# Generated by Django 4.1.6 on 2023-05-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familias', '0009_alter_familia_moradia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='casa_de',
            field=models.CharField(choices=[('Madeira', 'Madeira')], default='Casa', max_length=45),
        ),
        migrations.AlterField(
            model_name='familia',
            name='condicoes_casa',
            field=models.CharField(choices=[('Boas', 'Boas'), ('Ruins', 'Ruins')], default='Casa', max_length=45),
        ),
        migrations.AlterField(
            model_name='familia',
            name='moradia',
            field=models.CharField(choices=[('Casa', 'Casa')], default='Casa', max_length=45),
        ),
    ]