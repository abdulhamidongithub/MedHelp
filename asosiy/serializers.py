from rest_framework import serializers
from .models import *

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


# https://www.google.com/maps/search/?api=1&query=$latitude,$longitude
