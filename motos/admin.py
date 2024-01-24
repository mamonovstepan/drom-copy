from django.contrib import admin
from . import models as m

admin.site.register(m.MotorcycleClass)
admin.site.register(m.MotorcycleBrand)
admin.site.register(m.MotorcycleModel)


@admin.register(m.MotorcyclePost)
class MotoPostAdmin(admin.ModelAdmin):
    list_display = ['moto_brand', 'moto_model', 'year_of_issue',
                    'city','price', 'fuel', 'engine_capacity',
                    'stroke', 'moto_class', 'mileage']
