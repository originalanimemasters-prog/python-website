"""URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="DevForge API",
        default_version='v1',
        description="Developer platform API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/auth/', include('apps.accounts.urls')),
    path('api/v1/users/', include('apps.profiles.urls')),
    path('api/v1/problems/', include('apps.problems.urls')),
    path('api/v1/submissions/', include('apps.submissions.urls')),
    path('api/v1/challenges/', include('apps.challenges.urls')),
    path('api/v1/snippets/', include('apps.snippets.urls')),
    path('api/v1/projects/', include('apps.projects.urls')),
    path('api/v1/blogs/', include('apps.blogs.urls')),
    path('api/v1/community/', include('apps.community.urls')),
    path('api/v1/contests/', include('apps.contests.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/search/', include('apps.search.urls')),
    
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
