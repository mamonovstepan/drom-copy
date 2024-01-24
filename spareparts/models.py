from django.db import models
from cities.models import City
from django.contrib.auth.models import User


# Модель хранящая тип транспортного средства (авто, мото и т.д.)
class TypeOfTransport(models.Model):
    type = models.CharField(verbose_name='Тип транспорта', max_length=10)

    class Meta:
        verbose_name = 'Тип транспорта'
        verbose_name_plural = 'Типы транспорта'

    def __str__(self):
        return self.type


# Функция для составления пути сохранения фото в соответствии с пользователем
def upload_path(instance, filename):
    return f'SpareParts/{instance.author.username}/{filename}'


# Модель хранящая объявление о продаже запасной части
class SparePart(models.Model):
    CONDITION = [
        ('new', 'Новый'),
        ('old', 'Б/У'),
    ]

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Фото', upload_to=upload_path)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT)
    condition = models.CharField(verbose_name='Состояние', max_length=3, choices=CONDITION, default='new')
    fit_for = models.CharField(verbose_name='Подходит для', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=450)
    publication_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    type_of_transport = models.ForeignKey(TypeOfTransport, verbose_name='Тип транспорта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    def __str__(self):
        return f'{self.title} | {self.author}'
