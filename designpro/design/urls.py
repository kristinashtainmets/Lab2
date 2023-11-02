from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('applications/', views.ApplicationListView.as_view(), name='applications'),
    path('', views.home, name='home'),
    path('', views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
