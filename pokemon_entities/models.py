from django.db import models  # noqa F401


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True)
    title = models.CharField(max_length=200)
