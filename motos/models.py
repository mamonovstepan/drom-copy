from datetime import date
from django.db import models
from cities.models import City
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Список видов топлива для модели MotorcyclePost
FUEL = [
    ('n', 'Не указано'),
    ('g', 'Бензин'),
    ('e', 'Электро'),
]

# Список хранящий тактность мотора мотоцикла
STROKE = [
    ('n', 'Не указано'),
    ('2', '2-тактный'),
    ('4', '4-тактный'),
]

# Список хранящий состояние мотоцикла
CONDITION = [
    ('n', 'Не указано'),
    ('new', 'Новый'),
    ('old', 'Б/У'),
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


# Функция для составления пути сохранения фото в соответствии с пользователем
def upload_path(instance, filename):
    return f'SpareParts/{instance.author.username}/{filename}'


class MotorcyclePost(models.Model):
    moto_brand = models.ForeignKey(MotorcycleBrand, verbose_name='Марка мотоцикла', on_delete=models.PROTECT)
    moto_model = models.ForeignKey(MotorcycleModel, verbose_name='Модель мотоцикла', on_delete=models.PROTECT)
    year_of_issue = models.PositiveSmallIntegerField(verbose_name='Год выпуска', validators=[MaxValueValidator(date.today().year), MinValueValidator(1900)])
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    fuel = models.CharField(verbose_name='Тип топлива', max_length=1, choices=FUEL, default='n')
    engine_capacity = models.PositiveSmallIntegerField(verbose_name='Объем двигателя (куб. см.)', validators=[MaxValueValidator(2000), MinValueValidator(1)], null=True, blank=True)
    stroke = models.CharField(verbose_name='Количество тактов', max_length=1, choices=STROKE, default='n')
    moto_class = models.ForeignKey(MotorcycleClass, verbose_name='Класс мотоцикла', on_delete=models.PROTECT)
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    in_stock = models.BooleanField(verbose_name='Наличие', default=True)
    condition = models.CharField(verbose_name='Состояние', max_length=3, choices=CONDITION, default='new')
    pts = models.BooleanField(verbose_name='Наличие ПТС', default=True)
    is_damgaed = models.BooleanField(verbose_name='Певреждения (на ходу или нет)', default=True)
    on_sale = models.BooleanField(verbose_name='В продаже', default=True)
    image = models.ImageField(verbose_name='Фото', upload_to=upload_path, default='default.jpg')

    def __str__(self):
        return f'{self.moto_brand} {self.moto_model} | {self.year_of_issue} года выпуска'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
