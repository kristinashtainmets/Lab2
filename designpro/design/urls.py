from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),  # новый URL-маршрут для регистрации
    # Это означает, что когда пользователь переходит на страницу 'design/', Django будет использовать функцию index
    path('logout/', views.logout_view, name='logout'),  # новый URL-маршрут для выхода
]
