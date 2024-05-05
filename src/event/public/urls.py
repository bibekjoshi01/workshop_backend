from django.urls import path, include
from . views import PublicEventListAPIView

urlpatterns = [
    path("all-events", PublicEventListAPIView.as_view(), name="public-all-events")
]
