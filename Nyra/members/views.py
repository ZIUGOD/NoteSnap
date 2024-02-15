from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile
from notes.models import Note
from django import forms


class EmailUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=32,
        label="Primeiro nome",
        required=True,
    )
    last_name = forms.CharField(
        max_length=32,
        label="Último nome",
        required=True,
    )
    email = forms.EmailField(
        max_length=128,
        label="E-mail",
        required=True,
    )
    username = forms.CharField(
        max_length=16,
        label="Usuário",
        required=True,
    )
    password1 = forms.CharField(
        max_length=128,
        min_length=8,
        label="Senha",
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        max_length=128,
        min_length=8,
        label="Confirme a senha",
        widget=forms.PasswordInput,
        required=True,
    )

    class Meta:
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
    form_class = EmailUserCreationForm
    success_url = reverse_lazy("login_user")
    template_name = "members/signup.html"


class MemberLoginView(LoginView):
    template_name = "members/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home_page")
    authentication_form = AuthenticationForm


class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "members/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nyra_user"] = User.objects.filter(
            username=self.kwargs["username"]
        ).first()
        print(context)
        return context
