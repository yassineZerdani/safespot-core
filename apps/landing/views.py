import os
from django.http import HttpResponse
from django.shortcuts import render


def sitemap(request):
    base = os.environ.get("SITE_URL", "https://safespot.app")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{base}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>{base}/privacy/</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>
  <url><loc>{base}/terms/</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>
</urlset>"""
    return HttpResponse(xml, content_type="application/xml")


def landing(request):
    return render(request, "landing/index.html", {
        "web_app_url": os.environ.get("WEB_APP_URL", "https://safespot.app"),
    })


def privacy(request):
    return render(request, "landing/privacy.html")


def terms(request):
    return render(request, "landing/terms.html")
