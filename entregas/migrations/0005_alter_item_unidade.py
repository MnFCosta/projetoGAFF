# Generated by Django 3.2.9 on 2023-04-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entregas', '0004_alter_item_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unidade',
            field=models.IntegerField(db_column='calculo_unidade', default=0, editable=False),
        ),
    ]