import math
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Alert


def format_time_ago(dt):
    now = timezone.now()
    delta = now - dt
    sec = delta.total_seconds()
    if sec < 60:
        return "just now"
    if sec < 3600:
        return f"{int(sec / 60)} minutes ago"
    if sec < 86400:
        return f"{int(sec / 3600)} hours ago"
    if sec < 604800:
        return f"{int(sec / 86400)} days ago"
    return dt.strftime("%Y-%m-%d")


def haversine_km(lat1, lng1, lat2, lng2):
    """Distance in km between two points."""
    R = 6371
    to_rad = lambda d: (d * math.pi) / 180
    d_lat = to_rad(lat2 - lat1)
    d_lng = to_rad(lng2 - lng1)
    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(to_rad(lat1)) * math.cos(to_rad(lat2)) * math.sin(d_lng / 2) ** 2
    )
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def hash_ip(ip):
    h = 0
    for c in ip:
        h = (h << 5) - h + ord(c)
        h &= 0xFFFFFFFF
    return f"u_{abs(h):x}"


def get_client_ip(request):
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "unknown")


@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def alert_list_create(request):
    if request.method == "POST":
        return alert_create(request)
    return alert_list(request)


def alert_list(request):
    lat = float(request.GET.get("lat", 33.5731))
    lng = float(request.GET.get("lng", -7.5898))
    radius_km = float(request.GET.get("radius", 5))

    alerts = Alert.objects.all()
    filtered = [a for a in alerts if haversine_km(lat, lng, a.lat, a.lng) <= radius_km]

    data = []
    for a in filtered:
        item = {
            "id": str(a.id),
            "type": a.type,
            "description": a.description,
            "lat": a.lat,
            "lng": a.lng,
            "reportedAt": a.reported_at.isoformat(),
            "reportedAgo": format_time_ago(a.reported_at),
            "ipHash": a.ip_hash,
        }
        data.append(item)

    return Response(data)


def alert_create(request):
    type_val = request.data.get("type", "").strip()
    description = request.data.get("description", "").strip()
    lat = request.data.get("lat", 33.5731)
    lng = request.data.get("lng", -7.5898)

    if not type_val or not description:
        return Response(
            {"error": "Type and description are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    ip = get_client_ip(request)
    ip_hash = hash_ip(ip)

    alert = Alert.objects.create(
        type=type_val,
        description=description,
        lat=float(lat) if lat is not None else 33.5731,
        lng=float(lng) if lng is not None else -7.5898,
        ip_hash=ip_hash,
    )

    return Response({"success": True, "id": str(alert.id)}, status=status.HTTP_201_CREATED)
