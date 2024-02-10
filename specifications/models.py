from django.db import models
from cars import models as m


class CarSpecification(models.Model):
    car_barnd = models.ForeignKey(m.CarBrand, verbose_name='Марка авто', on_delete=models.PROTECT)
    car_model = models.ForeignKey(m.CarModel, verbose_name='Модель авто', on_delete=models.PROTECT)
    car_generation = models.ForeignKey(m.CarGeneration, verbose_name='Поколение', on_delete=models.PROTECT)
    car_equipment = models.ForeignKey(m.CarEquipment, verbose_name='Комплектация', on_delete=models.PROTECT)
    year_of_issue = models.models.PositiveSmallIntegerField(verbose_name='Год выпуска', validators=[MaxValueValidator(date.today().year), MinValueValidator(1900)])
