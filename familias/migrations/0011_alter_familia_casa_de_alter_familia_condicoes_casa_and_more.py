# Generated by Django 4.1.6 on 2023-05-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familias', '0010_alter_familia_casa_de_alter_familia_condicoes_casa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='casa_de',
            field=models.CharField(choices=[('Alvenaria', 'Alvenaria'), ('Madeira', 'Madeira'), ('Mista', 'Mista'), ('Barraco', 'Barraco')], default='Casa', max_length=45),
        ),
        migrations.AlterField(
            model_name='familia',
            name='condicoes_casa',
            field=models.CharField(choices=[('Excelente', 'Excelente'), ('Boa', 'Boa'), ('Ruim', 'Ruim'), ('Péssima', 'Péssima')], default='Casa', max_length=45),
        ),
        migrations.AlterField(
            model_name='familia',
            name='moradia',
            field=models.CharField(choices=[('Própria', 'Própria'), ('Alugada', 'Alugada')], default='Casa', max_length=45),
        ),
    ]