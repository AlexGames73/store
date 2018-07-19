from django.urls import path
from store import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import *


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loggin, name='login'),
    path('logout/', views.loggout, name='logout'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('email/', views.email, name='email'),
]
