from rest_framework import serializers
from .models import RefillCenter

class RefillCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefillCenter
        fields = '__all__'
