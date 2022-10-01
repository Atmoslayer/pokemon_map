# Generated by Django 3.1.14 on 2022-10-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20221001_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Описание покемона', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(default='Покемон', max_length=20, verbose_name='Имя на русском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='Pokemon', max_length=20, verbose_name='Имя на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='ポケモン', max_length=20, verbose_name='Имя на японском'),
        ),
    ]
