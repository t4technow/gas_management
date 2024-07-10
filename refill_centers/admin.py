from django.contrib import admin
from .models import RefillCenter

@admin.register(RefillCenter)
class RefillCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_details')
    search_fields = ('name', 'address')
