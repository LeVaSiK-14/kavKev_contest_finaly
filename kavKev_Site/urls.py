from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="KAVKEV API",
        default_version='v1',
        description="Kav&Kev api for contest and online shop",
        terms_of_service="",
        contact=openapi.Contact(email="lev201611@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
    path('api/', include('products.urls')),
    path('api/', include('order.urls')),
    path('api/', include('rest_auth.urls')),
    path('api/swagger/', schema_view.with_ui(), name='schema-json'),
]
