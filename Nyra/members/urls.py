from .views import MemberLoginView, MemberSignUpView
from django.urls import path

urlpatterns = [
    path("login_user/", MemberLoginView.as_view(), name="login_user"),
    path("signup_user/", MemberSignUpView.as_view(), name="signup_user"),
]
