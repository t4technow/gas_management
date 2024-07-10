from django.contrib import admin
from .models import Cylinder, CylinderType

@admin.register(CylinderType)
class CylinderTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')

@admin.register(Cylinder)
class CylinderAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'location', 'consumer', 'refill_center')
    list_filter = ('status', 'type')
    search_fields = ('location',)
