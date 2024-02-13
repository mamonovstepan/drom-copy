from datetime import date
from django.db import models
from cities.models import City
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Список видов топлива для модели CarPost
FUEL = [
    ('n', 'Не указано'),
    ('g', 'Бензин'),
    ('d', 'Дизель'),
    ('e', 'Электро'),
    ('h', 'Гибрид'),
]

# Список типов коробок переключения передач для модели CarPost
TRANSMISSION = [
    ('n', 'Не указано'),
    ('a', 'Автомат'),
    ('r', 'Робот'),
    ('v', 'Вариатор'),
    ('m', 'Механика'),
]

# Список типов привода для модели CarPost
DRIVE = [
    ('n', 'Не указано'),
    ('a', 'Полный'),
    ('r', 'Задний'),
    ('f', 'Передний'),
]

# Список расположения руля для модели CarPost
STEERING_WHEEL = [
    ('n', 'Не указано'),
    ('l', 'Левый'),
    ('r', 'Правый'),
]

# Список хранящий состояние автомобиля
CONDITION = [
    ('new', 'Новый'),
    ('old', 'Б/У'),
]

# Список хранящий страну-производитель автомобиля
COUNTRY = [
    ('n', 'Не указано'),
    ('RU', 'Россия'),
    ('JP', 'Япония'),
    ('DE', 'Германия'),
    ('KR', 'Корея'),
    ('US', 'США'),
    ('CN', 'Китай'),
    ('OTH', 'Остальные'),
]

""" Модели для хранения информации об автомобилях """


# Класс для хранения типа кузова
class ChassisType(models.Model):
    name = models.CharField(verbose_name='Кузов', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузовов'


# Класс для хранения значков
class CarIcon(models.Model):
    name = models.ImageField(verbose_name='Значок', unique=True,
                             upload_to='icons/')


# Класс для хранения марки
class CarBrand(models.Model):
    name = models.CharField(verbose_name='Марка', max_length=30, unique=True)
    icon = models.ForeignKey(CarIcon, verbose_name='Значок',
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


# Класс для хранения моделей авто
class CarModel(models.Model):
    name = models.CharField(verbose_name='Модель', max_length=60, unique=True)
    car_brand = models.ForeignKey(CarBrand, verbose_name='Марка',
                                  related_name='brand', max_length=15,
                                  on_delete=models.PROTECT)
    chassis_type = models.ForeignKey(ChassisType, verbose_name='Тип кузова',
                                     related_name='brand', max_length=15,
                                     on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


# Класс для хранения поколения модели авто
class CarGeneration(models.Model):
    name = models.CharField(verbose_name='Поколение', max_length=30, unique=True)
    car_model = models.ForeignKey(CarModel, verbose_name='Модель',
                                  related_name='generation', max_length=15,
                                  on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'


# Класс для хранения комплектации модели авто
class CarEquipment(models.Model):
    name = models.CharField(verbose_name='Комплектация', max_length=30, unique=True)
    car_generation = models.ForeignKey(CarGeneration, verbose_name='Поколение',
                                       related_name='equipment', max_length=50,
                                       on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'


# Функция для составления пути сохранения фото в соответствии с пользователем
def upload_path(instance, filename):
    return f'Cars/{instance.author.username}/{filename}'


# Класс для хранения объявления о продаже автомобиля
class CarPost(models.Model):
    car_brand = models.ForeignKey(CarBrand, verbose_name='Марка авто', on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, verbose_name='Модель авто', on_delete=models.PROTECT)
    car_generation = models.ForeignKey(CarGeneration, verbose_name='Поколение', on_delete=models.PROTECT)
    car_equipment = models.ForeignKey(CarEquipment, verbose_name='Комплектация', on_delete=models.PROTECT)
    country_of_origin = models.CharField(verbose_name='Страна производства', max_length=3, choices=COUNTRY, default='n')
    year_of_issue = models.PositiveSmallIntegerField(verbose_name='Год выпуска', validators=[MaxValueValidator(date.today().year), MinValueValidator(1900)])
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    fuel = models.CharField(verbose_name='Тип топлива', max_length=1, choices=FUEL, default='n')
    engine_capacity = models.DecimalField(verbose_name='Объем двигателя (л)', max_digits=2, decimal_places=1, null=True, blank=True)
    engine_power = models.PositiveSmallIntegerField(verbose_name='Мощность двигателя (л.с.)', validators=[MaxValueValidator(999), MinValueValidator(1)])
    transmission = models.CharField(verbose_name='Тип трансмиссии', max_length=1, choices=TRANSMISSION, default='n')
    drive = models.CharField(verbose_name='Тип привода', max_length=1, choices=DRIVE, default='n')
    chassis_type = models.ForeignKey(ChassisType, verbose_name='Тип кузова', on_delete=models.PROTECT)
    color = models.CharField(verbose_name='Цвет кузова', max_length=20)
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    steering_wheel = models.CharField(verbose_name='Расположение руля', max_length=1, choices=STEERING_WHEEL, default='n')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    condition = models.CharField(verbose_name='Состояние', max_length=3, choices=CONDITION, default='new')
    image = models.ImageField(verbose_name='Фото', upload_to=upload_path, default='default.jpg')
    pts = models.BooleanField(verbose_name='Наличие ПТС', default=True)
    is_damgaed = models.BooleanField(verbose_name='Повреждения (на ходу или нет)', default=False)
    on_sale = models.BooleanField(verbose_name='В продаже', default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.car_brand} {self.car_model} | {self.year_of_issue} года выпуска'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
