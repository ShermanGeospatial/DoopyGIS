from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.BasemapView.as_view(), name="basemap"),
    path('new/', views.BasemapNewView.as_view(), name="basemap_new"),
    path('index/', views.BasemapListView.as_view(), name='basemap_list'),
    path('pointset/', views.COGOPointSetListView.as_view(), name='cogopointset_listview'),
    path('<int:pk>/', views.COGOPointListView.as_view(), name='cogopoint_listview'),
]