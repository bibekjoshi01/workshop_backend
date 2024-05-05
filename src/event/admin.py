from django.contrib import admin
from .models import (
    Event,
    EventCategory,
    EventComment,
    EventFeedback,
    EventPlatform,
    EventSpeaker,
    EventTag,
)

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventComment)
admin.site.register(EventFeedback)
admin.site.register(EventPlatform)
admin.site.register(EventSpeaker)
admin.site.register(EventTag)