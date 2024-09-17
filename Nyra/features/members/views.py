from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django import forms
from ..notes.models import Note
from django.db.models import Q


class EmailUserCreationForm(UserCreationForm):
    """
    A form for user registration that includes additional fields for
    first name, last name, and email.
    """

    first_name = forms.CharField(
        max_length=32,
        label="First name",
        required=True,
    )
    last_name = forms.CharField(
        max_length=32,
        label="Last name",
        required=True,
    )
    email = forms.EmailField(
        max_length=128,
        label="E-mail",
        required=True,
    )
    username = forms.CharField(
        max_length=16,
        label="Username",
        required=True,
    )
    password1 = forms.CharField(
        max_length=128,
        min_length=8,
        label="Password",
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        max_length=128,
        min_length=8,
        label="Confirm Password",
        widget=forms.PasswordInput,
        required=True,
    )

    class Meta:
        """
        Meta options for the form EmailUserCreationForm.
        """

        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class MemberSignUpView(generic.CreateView):
    """
    A view for user registration.
    """

    form_class = EmailUserCreationForm
    template_name = "members/signup.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        """
        If the form is valid, save the new user and log them in.
        """
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class MemberLoginView(LoginView):
    """
    A view for user login.
    """

    template_name = "members/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home_page")
    authentication_form = AuthenticationForm


class UserProfileView(generic.TemplateView):
    """
    A view for displaying user profile information and their notes.
    Only accessible to authenticated users.
    """

    template_name = "members/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nyra_user = User.objects.filter(username=self.kwargs["username"]).first()
        context["nyra_user"] = nyra_user

        if nyra_user:
            if self.request.user == nyra_user:
                # Exibe todas as notas (privadas e públicas) se o dono do perfil estiver logado
                context["user_notes"] = Note.objects.filter(author=nyra_user)
            else:
                # Exibe apenas as notas públicas para visitantes
                context["user_notes"] = Note.objects.filter(
                    author=nyra_user, is_private=False
                )
        return context
