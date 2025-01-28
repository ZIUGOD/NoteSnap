"""
This module contains views for handling notes in the Nyra application.

The views in this module are responsible for creating, updating, deleting, and displaying notes.
"""

from django.contrib.auth.mixins import LoginRequiredMixin  # , UserPassesTestMixin
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import NoteForm
from .models import Note


class NoteCreateView(LoginRequiredMixin, CreateView):  # UserPassesTestMixin
    """
    View for creating a new note.

    Inherits from CreateView, LoginRequiredMixin, and UserPassesTestMixin.
    """

    # permission_denied_message = "You must be a superuser to create a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "notes/create_note.html"
    form_class = NoteForm
    success_url = reverse_lazy("home_page")

    def test_func(self):
        """
        Test if the user is a superuser.
        """
        return self.request.user.is_superuser


class NoteDetailView(DetailView):
    """
    View for displaying the details of a note.

    Inherits from DetailView and LoginRequiredMixin.
    """

    permission_denied_message = "You must be logged in to view a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "notes/detail_note.html"
    context_object_name = "note"

    def get_object(self, queryset=None):
        print("REQUEST:", self.request)
        note = super().get_object(queryset)
        if note.is_private and note.author != self.request.user:
            return redirect("note_list")
        return note


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing note.

    Inherits from UpdateView and LoginRequiredMixin.
    """

    permission_denied_message = "You must be logged in to update a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "notes/update_note.html"
    context_object_name = "note"
    form_class = NoteForm
    success_url = reverse_lazy("home_page")

    def get_queryset(self):
        """
        Returns the queryset of notes filtered by the current user.

        Only notes created by the current user can be updated.
        """
        return Note.objects.filter(author=self.request.user)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a note.

    Inherits from DeleteView and LoginRequiredMixin.
    """

    permission_denied_message = "You must be logged in to delete a note."
    login_url = reverse_lazy("login_user")
    model = Note
    template_name = "notes/index.html"
    context_object_name = "notes"
    success_url = reverse_lazy("home_page")

    def get_queryset(self):
        """
        Returns the queryset of notes filtered by the current user.

        Only notes created by the current user can be deleted.
        """
        return Note.objects.filter(author=self.request.user)


class NoteListView(ListView):
    """
    View for displaying a list of notes.

    Inherits from ListView.
    """

    model = Note
    template_name = "notes/index.html"
    ordering = "-created_at"
    context_object_name = "notes"
    paginate_by = 50

    def get_queryset(self):
        """Returns the queryset of notes filtered by the current user."""
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(Q(author=user) | Q(is_private=False))
        else:
            return Note.objects.filter(is_private=False)
