from django.db import models


# Модель хранящая области страны
class Region(models.Model):
    name = models.CharField(verbose_name='Область',
                              max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'


# Модель хранящая города страны
class City(models.Model):
    name = models.CharField(verbose_name='Город',
                            max_length=120, unique=True)
    region = models.ForeignKey(Region, verbose_name='Область',
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
