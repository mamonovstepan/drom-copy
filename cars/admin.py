from django.contrib import admin
from . import models as m

admin.site.register(m.ChassisType)
admin.site.register(m.CarBrand)
admin.site.register(m.CarModel)
admin.site.register(m.CarGeneration)
