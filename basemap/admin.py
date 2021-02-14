from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Basemap, COGOPoint, COGOPointSet

@admin.register(Basemap)
class BasemapAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'style', 'zoom',)

@admin.register(COGOPoint)
class COGOPointAdmin(OSMGeoAdmin):
    list_display = ('location', 'description', 'pointSet',)

@admin.register(COGOPointSet)
class COGOPointSetAdmin(OSMGeoAdmin):
    list_display = ('name',)


