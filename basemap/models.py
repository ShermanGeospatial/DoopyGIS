from django.contrib.gis.db import models

class Basemap(models.Model):

    name = models.CharField(max_length=100,unique=True)
    location = models.PointField()
    zoom = models.IntegerField(default=5)
    
    STYLE_LIST = (
        ('streets-v11', 'streets'),
        ('light-v10', 'light', ),
        ('dark-v10', 'dark', ),
        ('outdoors-v11', 'outdoors'),
        ('satellite-v9', 'satellite'),
    )

    style = models.CharField(max_length=100,choices=STYLE_LIST,default='streets')

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        
        return reverse('basemap', kwargs={'pk':self.pk})