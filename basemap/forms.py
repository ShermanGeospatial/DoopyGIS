from django.contrib.gis import forms
from .models import Basemap

class BasemapForm(forms.ModelForm):
    
    class Meta:
        model = Basemap
        fields = ['name', 'style', 'zoom', 'location']
        widgets = {
            'location':forms.HiddenInput(),
        }