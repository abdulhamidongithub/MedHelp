from rest_framework import serializers
from .models import *

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'
