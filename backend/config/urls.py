from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication APIs
    path("api/auth/", include("apps.accounts.urls")),

    # Problems APIs
    path("api/problems/", include("apps.problems.urls")),

    # Python Course APIs
    path("api/python/", include("apps.python_course.urls")),

    # Health Check API
    path("", include("apps.core.urls")),
]