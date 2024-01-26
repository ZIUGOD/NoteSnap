from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class MemberLoginView(LoginView):
    template_name = "members/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home_page")
