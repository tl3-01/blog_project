"""Defines URL patterns for accounts."""

from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
