from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoogleSocialAuthSerializer, LinkedInAuthSerializer


class GoogleSocialAuthView(GenericAPIView):
    """Google Social Auth API View"""

    permission_classes = [AllowAny]
    serializer_class = GoogleSocialAuthSerializer

    @transaction.atomic
    def post(self, request):
        """
        POST with 'auth_token'
        Send an idtoken as from google to get user information
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            validated_data = serializer.validated_data
            data = validated_data["auth_token"]
        except Exception as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class LinkedInSocialAuthView(GenericAPIView):
    serializer_class = LinkedInAuthSerializer
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
