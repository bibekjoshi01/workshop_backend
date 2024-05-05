from django.conf import settings
from src.user.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from src.user.utils.generate_username import generate_unique_user_username


def register_or_social_user(
    provider, email: str, first_name: str, last_name: str, photo
):
    try:
        registered_user = User.objects.get(email=email)
        if registered_user.is_customer:
            registered_user.is_email_verified = True
            registered_user.save()

            return {
                "email": registered_user.email,
                "tokens": registered_user.tokens,
                "id": registered_user.id,
                "is_active": registered_user.is_active,
                "mobile_no": registered_user.mobile_no,
                "is_email_verified": registered_user.is_email_verified,
                "is_phone_verified": registered_user.is_phone_verified,
            }
        else:
            raise AuthenticationFailed(
                detail=f"User with email {email} already exists. Please try with new email !"
            )

    except User.DoesNotExist:
        user_data = {
            "email": email,
            "first_name": first_name,
            "middle_name": "",
            "last_name": last_name,
            "password": settings.SOCIAL_SECRET,
            "username": generate_unique_user_username("customer"),
        }
        # user_data['photo'] = relative_save_path

        user = User.objects.create_customer(**user_data)
        user.auth_provider = provider
        user.is_active = True
        user.is_email_verified = True
        user.save()

        new_user = authenticate(email=email, password=settings.SOCIAL_SECRET)
        return {
            "email": new_user.email,
            "tokens": new_user.tokens,
            "id": new_user.id,
            "is_active": new_user.is_active,
            "mobile_no": new_user.mobile_no,
            "is_email_verified": new_user.is_email_verified,
            "is_phone_verified": new_user.is_phone_verified,
        }
