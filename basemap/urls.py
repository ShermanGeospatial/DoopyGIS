from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.basemap, name="basemap"),
    path(r'get_name/', views.get_name, name="get_name"),
    path(r'basemap_all/', views.basemap_all, name="basemap_all")
]