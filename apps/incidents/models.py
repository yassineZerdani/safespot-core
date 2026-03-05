from django.contrib.gis.db import models


class Incident(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ("theft", "Theft"),
        ("accident", "Accident"),
        ("fire", "Fire"),
        ("lighting", "Lighting"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=255)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPE_CHOICES)
    severity = models.IntegerField()
    location = models.PointField(srid=4326)
    source_url = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
