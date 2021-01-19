from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.BasemapToolbarView.as_view(), name="basemap_toolbar"),
    path('', views.BasemapListView.as_view(), name='basemap_list'),
]