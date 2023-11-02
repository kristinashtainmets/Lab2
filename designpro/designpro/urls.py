from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('design.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('superadmin/', admin.site.urls),
]

