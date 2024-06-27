"""
This module contains the model for the `Note` object.
"""

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField


class Note(models.Model):
    """
    Model for the `Note` object.
    """

    title = models.CharField(
        verbose_name="Title",
        max_length=128,
        unique=True,
        blank=False,
        null=False,
    )

    text = RichTextField(
        verbose_name="Text",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at: ",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at: ",
    )
    author = CurrentUserField(
        related_name="user_notes",
        on_delete=models.CASCADE,
    )
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)[:128]

    class Meta:
        """
        Meta options for the model `Note`.
        """

        ordering = ["-updated_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        get_latest_by = "updated_at"
        unique_together = ["title", "author"]
        indexes = [
            models.Index(fields=["title", "author"]),
        ]
        permissions = [
            ("can_view_note", "Can view note"),
            ("can_create_note", "Can create note"),
            ("can_update_note", "Can update note"),
            ("can_delete_note", "Can delete note"),
        ]
