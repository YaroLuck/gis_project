from django.urls import path

from roads.views import RoadsMapView

app_name = 'roads'

urlpatterns = [
    path("map/", RoadsMapView.as_view()),
]
