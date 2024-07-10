from rest_framework import viewsets
from .models import Cylinder, CylinderType
from .serializers import CylinderSerializer, CylinderTypeSerializer

class CylinderTypeViewSet(viewsets.ModelViewSet):
    queryset = CylinderType.objects.all()
    serializer_class = CylinderTypeSerializer

class CylinderViewSet(viewsets.ModelViewSet):
    queryset = Cylinder.objects.all()
    serializer_class = CylinderSerializer
