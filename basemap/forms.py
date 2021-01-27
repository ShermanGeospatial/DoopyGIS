from django.contrib.gis import forms
from .models import Basemap

class BasemapForm(forms.ModelForm):
    
    class Meta:
        model = Basemap
        fields = ['name', 'style', 'zoom', 'location']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control form-control nav-item'}),
            'style': forms.Select(attrs={'class': 'form-control form-control nav-item'}),
            'location':forms.HiddenInput(),
            'zoom':forms.HiddenInput(),
        }