from django.urls import path, include
from .views import register, login

urlpatterns = [
    path('api/auth/register/', register),
    path('api/auth/login/', login),
    # Other URLs...
]
