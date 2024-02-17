from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django import forms


class EmailUserCreationForm(UserCreationForm):
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
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


# class MemberSignUpView(generic.CreateView):
#     form_class = EmailUserCreationForm
#     success_url = reverse_lazy("login_user")
#     template_name = "members/signup.html"


class MemberLoginView(LoginView):
    template_name = "members/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home_page")
    authentication_form = AuthenticationForm


class UserProfileView(generic.TemplateView):
    template_name = "members/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nyra_user"] = User.objects.filter(
            username=self.kwargs["username"]
        ).first()
        print(context)
        return context
