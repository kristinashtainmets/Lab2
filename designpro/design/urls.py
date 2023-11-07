from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import AdminDashboardView, CategoryCreateView
from .views import ProfileView, CreateRequestView, \
 DeleteRequestView

urlpatterns = [
                  path('', views.ApplicationListView.as_view(), name='index'),
                  path('logout/', views.logout_view, name='logout'),
                  path('register/', views.register, name='register'),
                  path('login/', views.login_view, name='login'),
                  path('', views.home, name='home'),
                  path('profile/', ProfileView.as_view(), name='profile'),
                  path('create_request/', CreateRequestView.as_view(), name='create_request'),
                  path('delete_request/<int:pk>/', DeleteRequestView.as_view(), name='delete_request'),
                  path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
                  path('category/new/', CategoryCreateView.as_view(), name='category_new'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
