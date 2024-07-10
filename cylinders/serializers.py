from rest_framework import serializers
from .models import Cylinder, CylinderType

class CylinderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CylinderType
        fields = '__all__'

class CylinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cylinder
        fields = '__all__'
