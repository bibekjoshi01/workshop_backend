from django.urls import path, include
from .views import GoogleSocialAuthView, LinkedInSocialAuthView


urlpatterns = [
    path("google", GoogleSocialAuthView.as_view()),
    path("linkedin", LinkedInSocialAuthView.as_view()),
]
