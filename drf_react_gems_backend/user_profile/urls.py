from django.urls import path


from drf_react_gems_backend.user_profile.views import ApiCreateUserProfileView

urlpatterns = [
    path(
        "create/",
        ApiCreateUserProfileView.as_view(),
        name="api_create_user_profile_view",
    ),
]
