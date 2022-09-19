# Generated by Django 3.1.14 on 2022-09-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20220919_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(max_length=10, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(max_length=10, verbose_name='Долгота'),
        ),
    ]
