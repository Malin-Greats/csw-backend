from email.mime import base
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title='Council of Social Workers Portal API',
        default_version='v1',
        description='RESTFUL API for Council of Social Workers Portal',
        contact=openapi.Contact(email=settings.FROM_EMAIL),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('browsable-api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
