from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('login/',views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('notifications/', views.notifications, name='notifications'),
    path('homepage/<int:auth_id>/', views.homepage, name='homepage'),
]
