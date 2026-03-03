from rest_framework import serializers
from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    reportedAt = serializers.DateTimeField(source="reported_at", read_only=True)
    reportedAgo = serializers.CharField(read_only=True)
    ipHash = serializers.CharField(source="ip_hash", read_only=True)

    class Meta:
        model = Alert
        fields = [
            "id",
            "type",
            "description",
            "lat",
            "lng",
            "reportedAt",
            "reportedAgo",
            "ipHash",
        ]
        read_only_fields = ["reported_at", "ip_hash"]
