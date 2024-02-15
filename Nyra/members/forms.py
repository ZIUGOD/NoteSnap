from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import UserProfile


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(label="Primeiro Nome", max_length=16)
    last_name = forms.CharField(label="Último Nome", max_length=32)
    username = forms.CharField(label="Nome de Usuário", max_length=16)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="text-center form-group col-md-6 mb-0"),
                Column("last_name", css_class="text-center form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("username", css_class="form-group col-md-6 mb-0"),
                Column("email", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "password1",
            "password2",
            Submit("submit", "Cadastrar"),
        )


class BiographyForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["biography"]
