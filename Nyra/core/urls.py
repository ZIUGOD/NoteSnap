from django.contrib import admin
from django.urls import path, include
from notes.views import NoteListView

urlpatterns = [
    path("", NoteListView.as_view(), name="home_page"),
    path("admin/", admin.site.urls),
    path("note/", include("notes.urls")),
    path("", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
]
