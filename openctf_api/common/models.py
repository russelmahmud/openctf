from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        db_table = 'genders'

    def __str__(self) -> str:
        return self.name


class PlayerType(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'player_types'
        verbose_name = 'Player Type'
        verbose_name_plural = 'Player Types'

    def __str__(self) -> str:
        return self.name
