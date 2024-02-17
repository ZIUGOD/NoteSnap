from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path(
        "create/",
        login_required(NoteCreateView.as_view()),
        name="create_note",
    ),
    path(
        "<int:pk>/",
        # login_required(NoteDetailView.as_view()),
        NoteDetailView.as_view(),
        name="read_note",
    ),
    path(
        "<int:pk>/update/",
        login_required(NoteUpdateView.as_view()),
        name="update_note",
    ),
    path(
        "<int:pk>/delete/",
        login_required(NoteDeleteView.as_view()),
        name="delete_note",
    ),
]
