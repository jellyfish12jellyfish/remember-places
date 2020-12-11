from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'memories'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
