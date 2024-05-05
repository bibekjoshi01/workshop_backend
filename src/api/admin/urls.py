from django.urls import include
from django.urls import path

app_label = ["admin"]

urlpatterns = [path("", include("src.user.urls"))]
