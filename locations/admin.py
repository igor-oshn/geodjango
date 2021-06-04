from django.contrib import admin

from .models import Company, Device, Location

admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Device)
