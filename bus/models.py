from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from datetime import datetime
from django.utils import timezone
# Create your models here.

class FromTo(models.Model):
    _from = models.PointField(default='POINT(0 0)', srid=4326)
    from_short = models.CharField(max_length=50)
    _to = models.PointField(default='POINT(0 0)', srid=4326)
    to_short = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_from_lat(self):
        return self._from[0]

    @property
    def get_from_long(self):
        return self._from[1]

    @property
    def get_to_lat(self):
        return self._to[0]

    @property
    def get_to_long(self):
        return self._to[1]