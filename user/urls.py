from django.contrib.auth.views import PasswordChangeView, LoginView, PasswordChangeDoneView
from django.urls import path
from django.views.generic import TemplateView

from memories.views import UserRegistrationView

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(template_name="user/profile.html"), name='profile'),
    path('password_change/',
         PasswordChangeView.as_view(template_name="registration/change_password.html"), name='password_change')

    # path('login/', LoginView.as_view(), name='login'),
    # path('registration/', UserRegistrationView.as_view(), name='registration'),
    # path('password_change/done/',
    #      PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),
    #      name="password_change_done"),
]