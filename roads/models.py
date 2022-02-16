import random

from django.contrib.gis.db import models as geo_models
# from django.contrib.gis.geos import LineString, Point
# from django.contrib.gis.gdal.geometries import LineString
from django.contrib.gis.geos import LineString, Point
from django.db import models


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = geo_models.PointField()


class Road(models.Model):
    """ Дорога """

    name = models.CharField(max_length=255)

    location = geo_models.LineStringField(null=True, blank=True)

    coordinates_file = models.FileField(null=True, blank=True)

    @classmethod
    def add_road(cls):
        """
         Examples:
         ls = LineString((1, 1), (2, 2))
         ls = LineString([(1, 1), (2, 2)])
         ls = LineString(array([(1, 1), (2, 2)]))
         ls = LineString(Point(1, 1), Point(2, 2))
        """

        x_y_array = [(74.53125, 35.46067), (130.78125, 68.138852), (240.46875, 61.606396)]

        # line_string_object = LineString(x_y_array)
        print(LineString((0, 0), (1, 1), srid=4326))
        print(LineString(Point(1, 1), Point(2, 2), srid=4326))
        ls = LineString([(1, 1), (2, 2)], srid=4326)

        cls.objects.create(name=f'{random.randint(1,100)}', location=ls)
