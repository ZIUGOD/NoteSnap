"""
Forms for the members app.
"""

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """
    A form for user registration that includes additional fields for
        first name, last name, and email.
    """

    first_name = forms.CharField(
        label="First Name",
        max_length=16,
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=32,
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    username = forms.CharField(
        label="Username",
        max_length=16,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column(
                    "first_name",
                    css_class="text-center form-group col-md-6 mb-0",
                ),
                Column(
                    "last_name",
                    css_class="text-center form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            Row(
                Column("username", css_class="form-group col-md-6 mb-0"),
                Column("email", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "password1",
            "password2",
            Submit("submit", "Sign Up"),
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column(
                    "first_name",
                    css_class="text-center form-group col-md-6 mb-0",
                ),
                Column(
                    "last_name",
                    css_class="text-center form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            Row(
                Column("username", css_class="form-group col-md-6 mb-0"),
                Column("email", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "password1",
            "password2",
            Submit("submit", "Sign Up"),
        )


class BiographyForm(forms.ModelForm):
    """
    A form for user profile that includes additional fields for biography.
    """

    class Meta:
        """
        Meta options for the form BiographyForm.
        """

        model = UserProfile
        fields = ["biography"]
        widgets = {
            "biography": forms.Textarea(
                attrs={"placeholder": "Tell us about yourself..."}
            ),
        }
