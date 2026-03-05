from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Incident


@api_view(["POST"])
@permission_classes([AllowAny])
def incident_create(request):
    """
    Accept payload from AI scraper: title, incident_type, severity_score, lat, lng, source_url.
    """
    data = request.data
    title = data.get("title", "").strip()
    incident_type = (data.get("incident_type", "other") or "other").lower()
    severity_score = int(data.get("severity_score", 50))
    lat = float(data.get("lat", 0))
    lng = float(data.get("lng", 0))
    source_url = (data.get("source_url") or "").strip()[:500]

    if not title:
        return Response(
            {"error": "title is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    valid_types = [c[0] for c in Incident.INCIDENT_TYPE_CHOICES]
    if incident_type not in valid_types:
        incident_type = "other"

    point = Point(lng, lat, srid=4326)
    Incident.objects.create(
        title=title[:255],
        incident_type=incident_type,
        severity=min(100, max(0, severity_score)),
        location=point,
        source_url=source_url,
    )
    return Response({"success": True}, status=status.HTTP_201_CREATED)
