# Generated by Django 2.1.5 on 2021-01-23 15:29

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basemap', '0006_basemap_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemap',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name=django.contrib.gis.geos.point.Point(0.0, 0.0)),
        ),
        migrations.AlterField(
            model_name='basemap',
            name='name',
            field=models.CharField(default='Enter Map Name', max_length=100, unique=True),
        ),
    ]
