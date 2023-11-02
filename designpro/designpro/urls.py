from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('design.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # новый URL-маршрут для аутентификации
    path('admin/', admin.site.urls),
]

