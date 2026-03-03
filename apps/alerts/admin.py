from django.contrib import admin
from .models import Alert


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "description", "lat", "lng", "reported_at"]
    list_filter = ["type"]
    search_fields = ["description", "type"]
