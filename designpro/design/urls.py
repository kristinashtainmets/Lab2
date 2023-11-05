from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.ApplicationListView.as_view(), name='index'),
                  path('logout/', views.logout_view, name='logout'),
                  path('register/', views.register, name='register'),
                  path('login/', views.login_view, name='login'),
                  path('', views.home, name='home'),
                  path('profile/', ProfileView.as_view(), name='profile'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
