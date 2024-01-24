from django.contrib import admin
from . import models as m

admin.site.register(m.ChassisType)
admin.site.register(m.CarBrand)
admin.site.register(m.CarModel)
admin.site.register(m.CarGeneration)


@admin.register(m.CarPost)
class CarPostAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'car_model', 'year_of_issue',
                    'city', 'price', 'fuel', 'engine_capacity', 'transmission',
                    'drive', 'chassis_type', 'color', 'mileage', 'steering_wheel']
