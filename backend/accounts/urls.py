from django.urls import path
from .views import register, login_view, dashboard

urlpatterns = [
    path("register/", register),
    path("login/", login_view),
    path("dashboard/", dashboard),
]
