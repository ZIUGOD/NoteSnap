from django.db import models
from ckeditor.fields import RichTextField


class Note(models.Model):
    title = RichTextField(
        verbose_name="Título",
        unique=True,
        max_length=128,
    )

    text = RichTextField(
        verbose_name="Texto",
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at: ",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at: ",
    )

    def __str__(self):
        return self.title[:128]

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
