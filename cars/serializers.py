from .models import CarIcon
from rest_framework import serializers


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarIcon
        fields = ['name', 'car_brand']
