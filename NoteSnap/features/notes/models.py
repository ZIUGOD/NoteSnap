from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django_currentuser.db.models import CurrentUserField


class Note(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=128,
        blank=False,
        default="",
    )

    text = CKEditor5Field(
        "Text",
        config_name="extends",
        blank=False,
        null=False,

    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at: ",
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Updated at: ",
    )

    author = CurrentUserField(
        related_name="user_notes",
    )

    is_private = models.BooleanField(
        verbose_name="Is this note private?",
        default=False,
    )

    def __str__(self):
        return str(self.title)[:128]

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_note_title_author"
            ),
            models.UniqueConstraint(
                fields=["text", "author"], name="unique_note_text_author"
            ),
        ]
        indexes = [
            models.Index(fields=["title", "author"]),
        ]

    def save(self, *args, **kwargs):
        if self.pk: 
            old = Note.objects.get(pk=self.pk)
            if old.title != self.title or old.text != self.text:
                self.updated_at = timezone.now()
            else:
                self.updated_at = old.updated_at
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return f"/notes/{self.id}/"
