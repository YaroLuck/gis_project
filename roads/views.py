import json

from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from roads.models import Marker


class RoadsMapView(TemplateView):
    """Markers map view."""

    template_name = "roads/map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""

        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
        return context
