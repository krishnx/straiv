"""pms_integration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from bookings.views import PMSBookingsView, BookingCreateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="PMS Integration API",
        default_version='v1',
        description="API for fetching and mapping PMS bookings",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/integrations/pms/bookings/", PMSBookingsView.as_view(), name="pms-bookings-get"),
    path("api/integrations/pms/bookings/save/", BookingCreateView.as_view(), name="pms-bookings-save"),

    # Swagger/OpenAPI routes:
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
