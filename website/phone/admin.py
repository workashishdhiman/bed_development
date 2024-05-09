from django.contrib import admin
from .models import devices

@admin.register(devices)
class devicesModelAdmin(admin.ModelAdmin):
    list_display=['id','Name']