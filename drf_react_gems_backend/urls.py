from django.contrib import admin
from django.urls import path, include

#TODO fix profiles url to plural
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("drf_react_gems_backend.user_credentials.urls")),
    path("api/profile/", include("drf_react_gems_backend.user_profile.urls")),
    path("api/products/", include("drf_react_gems_backend.product.urls")),
]
