from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from django.views.generic import TemplateView

app_name = 'memories'

urlpatterns = [
    path('', TemplateView.as_view(template_name='memories/home.html'), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('memories/', views.PlaceListView.as_view(), name='memories'),
    path('memory/<int:pk>/', views.PlaceDetailView.as_view(), name='memory'),
    # path('map/', views.create_place, name='map'),
    path('map/', views.PlaceCreateView.as_view(), name='map'),
    path('delete/<int:pk>', views.PlaceDeleteView.as_view(), name='delete')
]
