from django.db import models
from cities.models import City
from django.contrib.auth.models import User


# Список хранящий тактность мотора мотоцикла
STROKE = [
    (2, '2-тактный'),
    (4, '4-тактный'),
]

""" Модели для хранения информации о мотоциклах """


# Модель для классификации мотоциклов
class MotorcycleClass(models.Model):
    name = models.CharField(verbose_name='Класс мотоцикла', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс мотоцикла'
        verbose_name_plural = 'Классы мотоциклов'


# Класс для хранения производителя
class MotorcycleBrand(models.Model):
    name = models.CharField(verbose_name='Марка', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


# Класс для хранения моделей мотоциклов
class MotorcycleModel(models.Model):
    name = models.CharField(verbose_name='Модель', max_length=60, unique=True)
    motorcicle_brand = models.ForeignKey(MotorcycleBrand, verbose_name='Марка',
                                         related_name='brand', max_length=15,
                                         on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
