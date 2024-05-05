import requests
from rest_framework.response import Response
from rest_framework import status


class Google:
    """
    The data google provides:
    #1
    {
        'azp': '911272971156-o88udnncs15cg6kbc5ju326qn0mq1kvj.apps.googleusercontent.com',
        'aud': '911272971156-o88udnncs15cg6kbc5ju326qn0mq1kvj.apps.googleusercontent.com',
        'sub': '103046475729885174452',
        'scope': 'openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email',
        'exp': '1687694608',
        'expires_in': '3596',
        'email': 'emailaddress@gmail.com',
        'email_verified': 'true',
        'access_type': 'online'
    }

    #2
    {
        'sub': '103046475729885174452',
        'name': 'Bibek Joshi',
        'given_name': 'Bibek',
        'family_name': 'Joshi',
        'picture': 'https://lh3.googleusercontent.com/a/AAcHTtcc7k4drl24FPAHPmft-oVctgrpYcNEsZjv_6Iu3g=s96-c',
        'email': 'email@gmail.com',
        'email_verified': True,
        'locale': 'en-GB'
    }
    """

    @staticmethod
    def validate(auth_token):
        try:
            payload = {"access_token": auth_token}

            token_info = requests.post(
                "https://oauth2.googleapis.com/tokeninfo", params=payload
            )

            profile_info = requests.post(
                "https://www.googleapis.com/oauth2/v3/userinfo", params=payload
            )

            if token_info.status_code == 200 and profile_info.status_code == 200:
                id_info = token_info.json()
                user_detail = profile_info.json()
                return user_detail, id_info
            else:
                raise Exception()
        except Exception as e:
            return Response(
                f"Token Expired or Invalid {e}", status=status.HTTP_400_BAD_REQUEST
            )
