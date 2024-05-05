from rest_framework.generics import ListAPIView
from ..models import Event
from . serializers import PublicEventListSerializer


class PublicEventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = PublicEventListSerializer