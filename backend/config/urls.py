from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # All API routes
    path("api/", include("apps.accounts.urls")),
]