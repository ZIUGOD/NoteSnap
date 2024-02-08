from django.urls import path
from .views import MemberLoginView, MemberSignUpView

urlpatterns = [
    path("login_user/", MemberLoginView.as_view(), name="login_user"),
    path("signup_user/", MemberSignUpView.as_view(), name="signup_user"),
    # path("logout_user", MemberLogoutView.as_view(), name="logout_user"),
]
