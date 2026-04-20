from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin


def home(request):
    return HttpResponse("Django API is running")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("api/", include("accounts.urls")),
]
