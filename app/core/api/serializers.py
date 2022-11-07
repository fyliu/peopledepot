from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

from core.models import Faq, Project, RecurringEvent, User, Faq_viewed


class UserSerializer(serializers.ModelSerializer):
    """Used to retrieve user info"""

    time_zone = TimeZoneSerializerField(use_pytz=False)

    class Meta:
        model = User
        fields = (
            "uuid",
            "username",
            "created_at",
            "updated_at",
            "email",
            "first_name",
            "last_name",
            "gmail",
            "preferred_email",
            "current_job_title",
            "target_job_title",
            "current_skills",
            "target_skills",
            "linkedin_account",
            "github_handle",
            "slack_id",
            "phone",
            "texting_ok",
            "time_zone",
        )
        read_only_fields = (
            "uuid",
            "created_at",
            "updated_at",
            "username",
            "email",
        )


class ProjectSerializer(serializers.ModelSerializer):
    """Used to retrieve project info"""

    class Meta:
        model = Project
        fields = (
            "uuid",
            "name",
            "description",
            "created_at",
            "updated_at",
            "completed_at",
            "github_org_id",
            "github_primary_repo_id",
            "github_primary_url",
            "hide",
            "slack_url",
            "google_drive_url",
            "google_drive_id",
            "hfla_website_url",
            "image_logo",
            "image_hero",
            "image_icon",
            "readme_url",
            "wiki_url",
        )
        read_only_fields = (
            "uuid",
            "created_at",
            "updated_at",
            "completed_at",
        )


class RecurringEventSerializer(serializers.ModelSerializer):
    """Used to retrieve recurring_event info"""

    class Meta:
        model = RecurringEvent
        fields = (
            "uuid",
            "name",
            "start_time",
            "duration_in_min",
            "video_conference_url",
            "additional_info",
            "project",
        )
        read_only_fields = (
            "uuid",
            "created_at",
            "updated_at",
        )


class FaqSerializer(serializers.ModelSerializer):
    """Used to retrieve faq info"""

    class Meta:
        model = Faq
        fields = (
            "uuid",
            "question",
            "answer",
            "tool_tip_name",
        )
        read_only_fields = ("uuid", "created_on", "last_updated")


class Faq_viewedSerializer(serializers.ModelSerializer):
    """
    Retrieve each date/time the specified FAQ is viewed
    """

    class Meta:
        model = Faq_viewed
        fields = (
            "uuid",
            "faq",
            "read",
        )
        # should faq be read only and should read be editable?
        read_only_fields = ("uuid", "read")
