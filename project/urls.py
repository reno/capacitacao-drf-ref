from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.urls import router as core_router
from users.urls import router as users_router

main_router = routers.DefaultRouter()
main_router.registry.extend(core_router.registry)
main_router.registry.extend(users_router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="Minha API",
        default_version='v1',
        description="...",
        contact=openapi.Contact(email="renan.modenese@estudante.ufla.br"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path(
        'swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    )
]

urlpatterns += main_router.urls