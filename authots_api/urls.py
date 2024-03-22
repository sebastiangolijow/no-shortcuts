from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Authors haven api",
        default_version="v1",
        description="API endpoint for authors haven api course",
        contact=openapi.Contact(email="api.imperfect@gmail.com"),
        license=openapi.License(name="Test"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "No Shortcuts"
admin.site.site_title = "No Shortcuts"
admin.site.index_title = "No Shortcuts"
