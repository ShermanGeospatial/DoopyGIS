from django.contrib.gis.db import models

class Basemap(models.Model):

    name = models.CharField(max_length=100)
    location = models.PointField()
    style = models.CharField(max_length=100)
    zoom = models.IntegerField()
    
    def __str__(self):

        return self.name

    