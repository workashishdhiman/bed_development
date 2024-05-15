from django.contrib import admin
from .models import Devices

@admin.register(Devices)
class devicesModelAdmin(admin.ModelAdmin):
    list_display=['id','Name']