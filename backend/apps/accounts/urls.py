from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    ForgotPasswordView,
    LoginView,
    LogoutView,
    MeView,
    PasswordChangeView,
    RegisterView,
    ResetPasswordView,
    VerifyEmailView,
    health_check,
)

urlpatterns = [
    # Health
    path("health/", health_check, name="health-check"),

    # Authentication
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path(
        "auth/verify-email/",
        VerifyEmailView.as_view(),
        name="verify-email",
    ),

    path(
        "auth/forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password",
    ),

    path(
        "auth/reset-password/",
        ResetPasswordView.as_view(),
        name="reset-password",
    ),

    path(
        "auth/password/change/",
        PasswordChangeView.as_view(),
        name="password_change",
    ),

    path(
        "auth/logout/",
        LogoutView.as_view(),
        name="logout",
    ),

    # User
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),
]