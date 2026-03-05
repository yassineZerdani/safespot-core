from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.landing),
    path("privacy/", views.privacy),
    path("terms/", views.terms),
    path("robots.txt", TemplateView.as_view(template_name="landing/robots.txt", content_type="text/plain")),
    path("sitemap.xml", views.sitemap),
]
