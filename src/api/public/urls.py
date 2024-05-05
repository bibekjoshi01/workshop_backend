from django.urls import path, include

app_label = ["public"]

urlpatterns = [
    path("social-auth/", include("src.user.social_auth.urls")),
    path("event-app/", include("src.event.public.urls")),
]
