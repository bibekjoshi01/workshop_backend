from rest_framework import serializers

from ..models import Event


class PublicEventListSerializer(serializers.ModelSerializer):
    organizer_full_name = serializers.CharField(source="organizer.get_full_name")
    category_name = serializers.CharField(source="category.name")
    event_datetime = serializers.DateTimeField(source="timestamp")
    no_of_attendees = serializers.SerializerMethodField()
    event_type = serializers.CharField(source="event_type_display")

    class Meta:
        model = Event
        fields = [
            "uuid",
            "slug",
            "organizer_full_name",
            "category_name",
            "title",
            "thumbnail",
            "event_type",
            "event_datetime",
            "duration",
            "location",
            "no_of_attendees",
        ]

    def get_no_of_attendees(self, obj):
        return 150
    