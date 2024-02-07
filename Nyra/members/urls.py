from django.urls import path
from . import views

urlpatterns = [
    path("login_user/", views.MemberLoginView.as_view(), name="login_user"),
    path("signup_user/", views.MemberSignUpView.as_view(), name="signup_user"),
]
