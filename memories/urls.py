from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'memories'

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('memories/', views.memories, name='memories'),
    path('memory/<int:pk>/', views.memory, name='memory'),
    path('map/', views.create_place, name='map'),

]
