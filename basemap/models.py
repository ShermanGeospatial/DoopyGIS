from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Basemap(models.Model):

    name = models.CharField(max_length=100,unique=True,default='Enter Map Name')
    location = models.PointField(geography=True, default=Point(0.0, 0.0))
    zoom = models.FloatField(default=5)
    
    STYLE_LIST = (
        ('streets-v11', 'streets'),
        ('light-v10', 'light', ),
        ('dark-v10', 'dark', ),
        ('outdoors-v11', 'outdoors'),
        ('satellite-v9', 'satellite'),
    )

    style = models.CharField(max_length=100,choices=STYLE_LIST,default='streets')

    thumbnail = models.ImageField(upload_to='', default='default_map.png')

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        
        return reverse('basemap', kwargs={'pk':self.pk})