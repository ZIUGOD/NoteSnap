from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from .forms import NoteForm
from .models import Note


class NoteCreateView(CreateView, LoginRequiredMixin):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "components/create_note.html"
    form_class = NoteForm
    success_url = reverse_lazy("home_page")


class NoteDetailView(DetailView, LoginRequiredMixin):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "components/detail_note.html"
    context_object_name = "note"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NoteUpdateView(UpdateView, LoginRequiredMixin):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "components/update_note.html"
    context_object_name = "note"
    form_class = NoteForm
    success_url = reverse_lazy("home_page")

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NoteDeleteView(DeleteView, LoginRequiredMixin):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "components/delete_note.html"
    context_object_name = "note"
    success_url = reverse_lazy("home_page")


class NoteListView(LoginRequiredMixin, ListView):
    permission_denied_message = "You must be logged in to create a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "notes/index.html"
    context_object_name = "note"
    ordering = ["-created_at"]

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
