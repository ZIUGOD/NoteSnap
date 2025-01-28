from django import forms
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django_currentuser.db.models import CurrentUserField


class Note(models.Model):
    """
    Model for the `Note` object.
    """

    title = models.CharField(
        verbose_name="Title",
        max_length=128,
        blank=False,
        default="",
    )

    text = CKEditor5Field(
        "Text content",
        config_name="extends",
        blank=False,
        null=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at: ",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name="Updated at: ",
    )

    author = CurrentUserField(
        related_name="user_notes",
        on_delete=models.CASCADE,
    )

    is_private = models.BooleanField(
        verbose_name="Is this note private?",
        default=False,
    )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        """
        Custom save method to ensure `created_at` is set on creation.
        """
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
        constraints = [
            models.UniqueConstraint(fields=["title", "author"], name="unique_note_title_author")
        ]
        indexes = [
            models.Index(fields=["title", "author"]),
        ]
