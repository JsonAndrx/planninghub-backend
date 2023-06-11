from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('login/access', TokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
