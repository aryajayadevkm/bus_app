from django.contrib.gis import admin
from django.contrib.gis.geos import GEOSGeometry
from bus.models import FromTo

# Register your models here.
class FromToAdmin(admin.OSMGeoAdmin):
    list_display = ['from_short', 'get_from_lat', 'get_from_long', 'to_short', 'get_to_lat', 'get_to_long']
    search_fields = ['from_short', 'to_short']

admin.site.register(FromTo, FromToAdmin)