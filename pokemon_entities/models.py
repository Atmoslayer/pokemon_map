from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(default='Покемон', max_length=35, verbose_name='Имя на русском')
    title_en = models.CharField(default='Pokemon', max_length=35, verbose_name='Имя на английском')
    title_jp = models.CharField(default='ポケモン', max_length=35, verbose_name='Имя на японском')
    description = models.TextField(default='Описание покемона', verbose_name='Описание')
    image = models.ImageField(null=True, verbose_name='Картинка')
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Из кого эволюционировал',
        related_name='next_evolution')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemons')
    appeared_at = models.DateTimeField(null=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Время исчезновения')
    lat = models.FloatField(max_length=10, verbose_name='Широта')
    lon = models.FloatField(max_length=10, verbose_name='Долгота')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

