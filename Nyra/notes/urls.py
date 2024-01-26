from django.urls import path
from .views import NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("create/", NoteCreateView.as_view(), name="create_note"),
    path("<int:pk>/", NoteDetailView.as_view(), name="read_note"),
    path("<int:pk>/update/", NoteUpdateView.as_view(), name="update_note"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="delete_note"),
]
