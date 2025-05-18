"""
This module defines the URL patterns for the Nyra application.

The urlpatterns list contains the following URL patterns:
- The root URL pattern maps to the NoteListView class from the features.notes.views module,
    serving as the home page.
- The empty path includes the URL patterns for authentication provided by the
    `django.contrib.auth.urls` module.
- The "admin/" path maps to the Django admin site.
- The "note/" path includes the URL patterns defined in the features.notes.urls module.
- The "u/" path includes the URL patterns defined in the features.members.urls module.
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from features.notes.views import NoteListView

urlpatterns = [
    path("", NoteListView.as_view(), name="home_page"),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("note/", include("features.notes.urls", namespace="note")),
    path("u/", include("features.members.urls", namespace="member")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
