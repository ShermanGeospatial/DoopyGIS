# Generated by Django 2.1.5 on 2021-02-09 16:35

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basemap', '0013_auto_20210209_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cogopoint',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0, 0.0), srid=4326),
        ),
    ]
