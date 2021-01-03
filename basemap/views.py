from django.shortcuts import render
from .forms import BasemapForm
from .models import Basemap

def basemap(request):

    basemapAll = Basemap.objects.all()

    return render(request, 'basemap.html', {'basemap_current': basemapAll[0]})

def basemap_all(request):

    basemapAll = Basemap.objects.all()
    print(basemapAll[0].name)
    return render(request, 'basemap_all.html', {'basemap_all': basemapAll})

def get_name(request):

    form = BasemapForm()
        
    return render(request, 'name.html', {'form': form})
    

