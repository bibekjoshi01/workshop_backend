import requests
from rest_framework import status
from rest_framework.response import Response


class LinkedIn:
    @staticmethod
    def get_member_details(access_token):
        try:
            # Set the Authorization header with the access token
            headers = {"Authorization": f"Bearer {access_token}"}

            # Make a GET request to the LinkedIn userinfo endpoint
            response = requests.get(
                "https://api.linkedin.com/v2/userinfo", headers=headers
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response to get member details
                member_details = response.json()
                return member_details
            else:
                return Response(
                    f"LinkedIn API request failed with status code {response.status_code}",
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                f"Token Expired or Invalid: {e}", status=status.HTTP_400_BAD_REQUEST
            )
