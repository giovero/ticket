from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("ticket/", include("ticket.urls")),
    path("login/", include("login.urls")),
    path("admin/", admin.site.urls),
]
