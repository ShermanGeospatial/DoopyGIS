from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Basemap

@admin.register(Basemap)
class BasemapAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'style', 'zoom')


