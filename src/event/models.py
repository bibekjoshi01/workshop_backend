import uuid
from django.db import models
from django.utils.text import slugify
from .constants import EVENT_STATUS, EVENT_TYPES, PLATFORM_CHOICES

class EventCategory(models.Model):
    """
    Represents a category of events.
    """

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100, unique=True, help_text="Name of the event category"
    )
    icon = models.ImageField(null=True, upload_to="event_category/")
    description = models.TextField(
        max_length=255, blank=True, help_text="Description of the event category"
    )
    is_active = models.BooleanField(
        default=True, help_text="Whether the category is active or not"
    )

    def __str__(self) -> str:
        return self.name


class EventPlatform(models.Model):
    """
    Represents a platform used for hosting events.
    """

    name = models.CharField(
        max_length=100,
        choices=PLATFORM_CHOICES,
        unique=True,
        help_text="Name of the platform",
    )
    link = models.URLField(max_length=200, blank=True, help_text="link of the event")
    logo = models.ImageField(
        upload_to="platform_logos/",
        null=True,
        blank=True,
        help_text="Logo of the platform in case of other than standard",
    )

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    """
    Represents an event.
    """

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        EventCategory,
        on_delete=models.PROTECT,
        related_name="events",
        help_text="Category of the event",
    )
    organizer = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="organized_events",
        help_text="User who organized the event",
    )
    title = models.CharField(max_length=255, help_text="Title of the event")
    slug = models.SlugField(unique=True, max_length=300)
    description = models.TextField(blank=True, help_text="Description of the event")
    thumbnail = models.ImageField(
        upload_to="event_thumbnails/",
        null=True,
        blank=True,
        help_text="Thumbnail image for the event",
    )
    event_type = models.CharField(
        choices=EVENT_TYPES, max_length=30, help_text="Type of the event"
    )
    timestamp = models.DateTimeField(help_text="Date and time of the event")
    duration = models.DurationField(help_text="Duration of the event")
    location = models.CharField(
        max_length=255, blank=True, help_text="Location of the event (if in person)"
    )
    status = models.CharField(
        choices=EVENT_STATUS,
        max_length=30,
        default="draft",
        help_text="Status of the event",
    )
    is_approved = models.BooleanField(
        default=False, help_text="Whether the event is approved by admin or not"
    )
    max_capacity = models.PositiveIntegerField(
        default=0, help_text="Maximum capacity of attendees"
    )
    allow_comments = models.BooleanField(
        default=True, help_text="Whether comments are allowed for the event"
    )
    created_date = models.DateTimeField(
        auto_now_add=True, help_text="Date and time when the event was created"
    )
    updated_date = models.DateTimeField(
        auto_now=True, help_text="Date and time when the event was last updated"
    )

    def __str__(self) -> str:
        return self.title


class EventComment(models.Model):
    """
    Represents a comment on an event.
    """

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="event_comments",
        help_text="User who posted the comment",
    )
    message = models.TextField(help_text="Content of the comment")
    reply = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        help_text="Optional reply to another comment",
    )
    reaction = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Reaction to the comment (e.g., like, love, etc.)",
    )
    is_hidden = models.BooleanField(
        default=False, help_text="Whether the comment is hidden by the organizer"
    )
    platform = models.OneToOneField(
        EventPlatform,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="event",
        help_text="Platform used for the event",
    )
    created_date = models.DateTimeField(
        auto_now_add=True, help_text="Date and time when the comment was created"
    )
    updated_date = models.DateTimeField(
        auto_now=True, help_text="Date and time when the comment was last updated"
    )
    is_archived = models.BooleanField(
        default=False, help_text="Whether the comment is archived"
    )

    def save(self, *args, **kwargs):
        # Slugify the title
        slug = slugify(self.title)
        # Check if there's already an event with this slug
        if Event.objects.filter(slug=slug).exists():
            # Append UUID to make it unique
            slug = f"{slug}-{self.uuid}"
        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Comment by {self.user} on {self.created_date}"


class EventTag(models.Model):
    """
    Represents a tag associated with an event.
    """

    title = models.CharField(max_length=100, unique=True, help_text="Title of the tag")
    events = models.ManyToManyField(
        Event,
        related_name="tags",
        blank=True,
        help_text="Events associated with this tag",
    )

    def __str__(self) -> str:
        return self.title


class EventSpeaker(models.Model):
    """
    Represents a speaker at an event.
    """

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="speakers",
        help_text="Event for which the speakek is related",
    )
    photo = models.ImageField(
        upload_to="speaker_photos/",
        null=True,
        blank=True,
        help_text="Photo of the speaker",
    )
    full_name = models.CharField(max_length=100, help_text="Full name of the speaker")
    tagline = models.CharField(
        max_length=200, blank=True, help_text="Tagline or title of the speaker"
    )
    about = models.TextField(blank=True, help_text="Description or bio of the speaker")

    def __str__(self) -> str:
        return self.full_name


class EventFeedback(models.Model):
    """
    Represents feedback for an event.
    """

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="feedbacks",
        help_text="Event for which the feedback is provided",
    )
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="event_feedback",
        help_text="User providing the feedback",
    )
    rating = models.PositiveSmallIntegerField(help_text="Rating provided by the user")
    comment = models.TextField(
        blank=True, help_text="Optional comment or review by the user"
    )
    created_date = models.DateTimeField(
        auto_now_add=True, help_text="Date and time when the feedback was provided"
    )

    def __str__(self) -> str:
        return f"Feedback for {self.event} by {self.user}"
