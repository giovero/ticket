from django.urls import path
from login.views import obtain_auth_token

urlpatterns = [
    path("token/", obtain_auth_token, name="obtain-auth-token"),
]
