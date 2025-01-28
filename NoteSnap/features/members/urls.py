"""
This file contains the URL patterns for the members app.
"""

from django.urls import path
from .views import MemberLoginView, UserProfileView, MemberSignUpView

app_name = "member"

urlpatterns = [
    path("login_user/", MemberLoginView.as_view(), name="login_user"),
    path("signup_user/", MemberSignUpView.as_view(), name="signup_user"),
    path("<str:username>/", UserProfileView.as_view(), name="user_profile"),
]
