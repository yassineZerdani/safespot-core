from django.contrib.gis.db import models


class Incident(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ("theft", "Theft"),
        ("accident", "Accident"),
        ("lighting", "Lighting"),
    ]

    title = models.CharField(max_length=255)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPE_CHOICES)
    severity = models.IntegerField()
    location = models.PointField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
