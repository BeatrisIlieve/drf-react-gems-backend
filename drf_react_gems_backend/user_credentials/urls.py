from django.urls import path


from drf_react_gems_backend.user_credentials.views import (
    RegisterUserApiView,
    LoginUserApiView,
    UserEmailCheckApiView,
)

urlpatterns = [
    path(
        "register/",
        RegisterUserApiView.as_view(),
        name="register_user_api_view",
    ),
    path(
        "login/",
        LoginUserApiView.as_view(),
        name="login_user_api_view",
    ),
    path(
        "email-check/",
        UserEmailCheckApiView.as_view(),
        name="email_check",
    ),
]
