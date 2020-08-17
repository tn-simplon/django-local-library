"""localLibrary URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    # Add django site authentification urls
    path('accounts/', include('django.contrib.auth.urls')),
]
