from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя на русском')
    title_en = models.CharField(null=True, max_length=20, verbose_name='Имя на английском')
    title_jp = models.CharField(null=True, max_length=20, verbose_name='Имя на японском')
    description = models.CharField(null=True, max_length=400, verbose_name='Описание')
    image = models.ImageField(null=True, verbose_name='Картинка')
    appeared_at = models.DateTimeField(null=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Время исчезновения')
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='В кого эволюционирует')
    level = models.IntegerField(null=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(max_length=50)
    lon = models.FloatField(max_length=50)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)