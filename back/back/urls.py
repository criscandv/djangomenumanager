from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static

from apps.api.utils import CustomObtainJSONWebToken
from apps.api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('api/auth/', CustomObtainJSONWebToken.as_view()),

    # Api endpoints
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
