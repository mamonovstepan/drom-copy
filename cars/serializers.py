from .models import CarIcon
from rest_framework import serializers


class IconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarIcon
        fields = ['name', 'car_brand']
