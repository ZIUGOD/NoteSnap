"""
This file contains the URL patterns for the notes app.
"""

from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView

app_name = "note"

urlpatterns = [
    path(
        "create/",
        login_required(NoteCreateView.as_view()),
        name="create_note",
    ),
    path(
        "<int:pk>/",
        NoteDetailView.as_view(),
        name="read_note",
    ),
    path(
        "update/<int:pk>/",
        login_required(NoteUpdateView.as_view()),
        name="update_note",
    ),
    path(
        "delete/<int:pk>/",
        login_required(NoteDeleteView.as_view()),
        name="delete_note",
    ),
]
