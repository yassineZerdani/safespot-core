from django.urls import path
from . import views

urlpatterns = [
    path("alerts/", views.alert_list_create),
]
