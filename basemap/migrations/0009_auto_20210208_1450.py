# Generated by Django 2.1.5 on 2021-02-08 14:50

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basemap', '0008_auto_20210123_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='COGOLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', django.contrib.gis.db.models.fields.LineStringField(geography=True, srid=4326)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='COGOPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), geography=True, srid=4326)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='COGOPointSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='COGOPolygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='basemap',
            name='notes',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='cogopoint',
            name='pointSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basemap.COGOPointSet'),
        ),
    ]
