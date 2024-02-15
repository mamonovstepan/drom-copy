from rest_framework import generics
from .models import CarIcon
from .serializers import IconsSerializer


class IconsView(generics.ListAPIView):
    queryset = CarIcon.objects.all()
    serializer_class = IconsSerializer
