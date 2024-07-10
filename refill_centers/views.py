from rest_framework import viewsets
from .models import RefillCenter
from .serializers import RefillCenterSerializer

class RefillCenterViewSet(viewsets.ModelViewSet):
    queryset = RefillCenter.objects.all()
    serializer_class = RefillCenterSerializer
