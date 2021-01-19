from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import Basemap
from .forms import BasemapForm
from django.contrib.gis import forms

class BasemapView(generic.DetailView):

    model = Basemap
    template_name = 'basemap/basemap.html'

class BasemapToolbarView(generic.UpdateView):

    model = Basemap
    template_name = 'basemap/basemap_toolbar.html'
    success_url = reverse_lazy('basemap_list')
    form_class = BasemapForm

class BasemapListView(generic.ListView):

    template_name = 'basemap/basemap_listview.html'
    context_object_name = 'basemap_listview'

    def get_queryset(self):

        return Basemap.objects.all()