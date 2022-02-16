from decimal import Decimal
from sys import getsizeof

from django.contrib.gis import admin as geo_admin
from django.contrib.gis.geos import LineString, Point
from leaflet.admin import LeafletGeoAdmin

from roads.models import Marker, Road

@geo_admin.action(description='Тест точки')
def make_published1(modeladmin, request, queryset):
    for object in queryset:
        line_string_obj = Road.objects.last().location
        _point = line_string_obj.array[100]
        object.location = Point(_point)
        object.save()

@geo_admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")

    actions = [make_published1]


@geo_admin.action(description='Загрузить координаты из файла')
def make_published(modeladmin, request, queryset):
    for object in queryset:
        _file = object.coordinates_file
        with _file.open() as f:
            data = f.readlines()
        x_y_list = []
        for line in data:
            str_line = line.decode("utf-8")
            list_line = str_line.split(",")
            y = Decimal(list_line[1]) # !!!!
            x = Decimal(list_line[2])
            x_y_list.append((x, y))
        print(x_y_list)
        # [(1, 1), (2, 2)], srid = 4326
        line_string_obj = LineString(x_y_list, srid=4326)
        object.location = line_string_obj
        object.save()

@geo_admin.register(Road)
class MarkerAdmin(LeafletGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location", 'coordinates_file')

    actions = [make_published]
