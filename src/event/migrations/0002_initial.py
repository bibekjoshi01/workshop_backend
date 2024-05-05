# Generated by Django 4.2 on 2024-05-03 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("event", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="eventfeedback",
            name="user",
            field=models.ForeignKey(
                help_text="User providing the feedback",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_feedback",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="eventcomment",
            name="platform",
            field=models.OneToOneField(
                blank=True,
                help_text="Platform used for the event",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="event",
                to="event.eventplatform",
            ),
        ),
        migrations.AddField(
            model_name="eventcomment",
            name="reply",
            field=models.ForeignKey(
                blank=True,
                help_text="Optional reply to another comment",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="event.eventcomment",
            ),
        ),
        migrations.AddField(
            model_name="eventcomment",
            name="user",
            field=models.ForeignKey(
                help_text="User who posted the comment",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.ForeignKey(
                help_text="Category of the event",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="events",
                to="event.eventcategory",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="organizer",
            field=models.ForeignKey(
                help_text="User who organized the event",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organized_events",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
