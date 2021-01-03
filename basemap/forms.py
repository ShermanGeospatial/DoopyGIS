from django.contrib.gis import forms
from .models import Basemap

class BasemapForm(forms.Form):
    
    class Meta:
        model = Basemap
        fields = ('name', 'location', 'style', 'zoom')
        