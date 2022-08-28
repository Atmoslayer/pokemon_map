from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(max_length=50)
    lon = models.FloatField(max_length=50)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)