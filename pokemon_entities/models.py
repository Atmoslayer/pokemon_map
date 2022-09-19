from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(default='', max_length=20, verbose_name='Имя на русском')
    title_en = models.CharField(default='', max_length=20, verbose_name='Имя на английском')
    title_jp = models.CharField(default='', max_length=20, verbose_name='Имя на японском')
    description = models.TextField(default='', verbose_name='Описание')
    image = models.ImageField(null=True, verbose_name='Картинка')
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Из кого эволюционирует',
        related_name='pokemons')
    next_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='В кого эволюционирует')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
    appeared_at = models.DateTimeField(null=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Время исчезновения')
    lat = models.FloatField(max_length=10, verbose_name='Широта')
    lon = models.FloatField(max_length=10, verbose_name='Долгота')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')