# Generated by Django 2.1.5 on 2021-01-23 15:31

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basemap', '0007_auto_20210123_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemap',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), geography=True, srid=4326),
        ),
    ]
