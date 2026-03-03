from django.contrib.gis.admin import GISModelAdmin
from django.contrib import admin

from .models import Incident


@admin.register(Incident)
class IncidentAdmin(GISModelAdmin):
    list_display = ("title", "incident_type", "severity", "created_at")
    list_filter = ("incident_type", "severity")
