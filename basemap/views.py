from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import BasemapForm
from django.contrib.gis import forms

class BasemapView(generic.UpdateView):

    model = Basemap
    template_name = 'basemap/basemap_toolbar.html'
    form_class = BasemapForm
    success_url = reverse_lazy('basemap_list')

class BasemapNewView(generic.CreateView):

    model = Basemap
    template_name = 'basemap/basemap_toolbar.html'
    success_url = reverse_lazy('basemap_list')
    form_class = BasemapForm

class BasemapListView(generic.ListView):

    template_name = 'basemap/basemap_listview.html'
    context_object_name = 'basemap_listview'

    def get_queryset(self):

        return Basemap.objects.all()

class COGOPointSetListView(generic.ListView):

    template_name = 'basemap/cogopointset_listview.html'
    context_object_name = 'cogopointset_listview'

    def get_queryset(self):

        return COGOPointSet.objects.all()

class COGOPointListView(generic.ListView):

    context_object_name = 'cogopoint_listview'

    def get_queryset(self):

        return COGOPoint.objects.all()

