from django.contrib.gis.db import models
from django.contrib.gis.geos import Point, LineString, Polygon

#A model class for coordinate geometry points from land survey data containing PNEZD formatted data
class COGOPoint(models.Model):
    
    setID = models.IntegerField(default=-1)
    description = models.CharField(max_length=100,default='None')
    pointSet = models.ForeignKey('COGOPointSet',on_delete=models.CASCADE)
    location = models.PointField(geography=False, dim=2, default=Point(0.0, 0.0, 0.0))

    @property
    def getGeoJson(self):

        return list(getattr(self.location, 'coords', [])[::-1])

    def __str__(self):

        return self.description + ' ' + str(list(getattr(self.location, 'coords', [])[::-1]))

class COGOPointSet(models.Model):

    name = models.CharField(max_length=100,unique=True,default='None')

    def __str__(self):

        return self.name

class COGOLine(models.Model):

    line = models.LineStringField(geography=True)
    description = models.CharField(max_length=100,default='None')

class COGOPolygon(models.Model):

    polygon = models.PolygonField(geography=True)
    description = models.CharField(max_length=100,default='None')

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
    notes = models.TextField(default="None")
    thumbnail = models.ImageField(upload_to='', default='default_map.png')
    pointsets = models.ManyToManyField(COGOPointSet, blank=True)

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        
        return reverse('basemap', kwargs={'pk':self.pk})

    @property
    def get_pointsets(self):

        return self.pointsets

    @property
    def get_centre(self):

        return list(getattr(self.location, 'coords', [])[::-1])

    @property
    def get_srid(self):

        return self.location.srid

