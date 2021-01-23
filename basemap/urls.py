from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.BasemapToolbarView.as_view(), name="basemap_toolbar"),
    path('new/', views.BasemapNewToolbarView.as_view(), name="basemap_toolbar_new"),
    path('', views.BasemapListView.as_view(), name='basemap_list'),
]