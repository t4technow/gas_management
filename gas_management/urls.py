from baton.autodiscover import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cylinders.views import CylinderViewSet, CylinderTypeViewSet
from consumers.views import ConsumerViewSet
from refill_centers.views import RefillCenterViewSet

router = DefaultRouter()
router.register(r'cylinders', CylinderViewSet)
router.register(r'cylinder-types', CylinderTypeViewSet)
router.register(r'consumers', ConsumerViewSet)
router.register(r'refill-centers', RefillCenterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('api/', include(router.urls)),
]
