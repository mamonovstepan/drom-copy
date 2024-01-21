from django.db import models

""" Модели для хранения информации об автомобилях """


# Класс для хранения типа кузова
class ChassisType(models.Model):
    name = models.CharField(verbose_name='Кузов', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузовов'


# Класс для хранения марки
class CarBrand(models.Model):
    name = models.CharField(verbose_name='Марка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


# Класс для хранения моделей авто
class CarModel(models.Model):
    name = models.CharField(verbose_name='Модель')
    car_brand = models.ForeignKey(CarBrand, verbose_name='Марка',
                                  related_name='brand', max_length=15,
                                  on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


# Класс для хранения поколения модели авто
class CarGeneration(models.Model):
    name = models.CharField(verbose_name='Поколение')
    car_model = models.ForeignKey(CarModel, verbose_name='Модель',
                                  related_name='generation', max_length=15,
                                  on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'


# Класс для хранения объявления о продаже автомобиля
class CarPost(models.Model):
    pass
