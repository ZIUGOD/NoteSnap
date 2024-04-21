from django.db import models
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField


class Note(models.Model):
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

    def __str__(self):
        return self.title[:128]

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"
