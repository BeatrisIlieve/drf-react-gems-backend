from django.urls import path


from drf_react_gems_backend.user_credentials.views import ApiRegisterUserView

urlpatterns = [
    path(
        "register/",
        ApiRegisterUserView.as_view(),
        name="api_register_user_view",
    ),
]
