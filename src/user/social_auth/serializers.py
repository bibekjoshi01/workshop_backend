from rest_framework import serializers
from . import google
from config import settings
from rest_framework.exceptions import AuthenticationFailed
from .register import register_or_social_user

"""Google Social Auth Serializer"""


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_detail, id_info = google.Google.validate(auth_token)

        try:
            id_info["sub"]
        except:
            raise serializers.ValidationError({"message": "Invalid token !"})

        if id_info["aud"] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed({"message": "Authentication Failed aud!"})

        email = user_detail["email"]
        first_name = user_detail.get("given_name", "")
        last_name = user_detail.get("family_name", "")
        photo = user_detail.get("picture", None)
        provider = "GOOGLE"

        return register_or_social_user(
            provider=provider,
            email=email,
            first_name=first_name,
            last_name=last_name,
            photo=photo,
        )


class LinkedInAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_detail = linkedin.LinkedIn.get_member_details(auth_token)

        try:
            user_detail["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )

        email = user_detail["email"]
        full_name = user_detail.get("name", "")
        first_name = user_detail.get("given_name", "")
        last_name = user_detail.get("family_name", "")
        photo = user_detail.get("picture", None)
        provider = "linkedin"

        return register_or_social_user(
            provider=provider,
            email=email,
            first_name=first_name,
            last_name=last_name,
            photo=photo,
        )

    def to_representation(self, instance):
        return super().to_representation(instance)
