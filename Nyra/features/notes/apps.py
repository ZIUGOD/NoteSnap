"""
This file is used to configure the notes app.
"""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """
    Configuration for the notes app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "features.notes"
