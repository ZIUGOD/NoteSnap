from django.contrib import admin
from django.urls import path, include
from features.notes.views import NoteListView

urlpatterns = [
    path("", NoteListView.as_view(), name="home_page"),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("note/", include("features.notes.urls")),
    path("members/", include("features.members.urls")),
]
