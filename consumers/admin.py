from django.contrib import admin
from .models import Consumer

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_details')
    search_fields = ('name', 'address')
