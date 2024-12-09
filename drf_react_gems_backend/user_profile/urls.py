from django.urls import path


from drf_react_gems_backend.user_profile.views import UserProfileApiView

urlpatterns = [
    path(
        "create/",
        UserProfileApiView.as_view(),
        name="user_profile_api_view",
    ),
]
