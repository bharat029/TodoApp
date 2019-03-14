from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.UserRegistrationFormView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout')
]