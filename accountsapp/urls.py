from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.registration, name='registration'),
    path('logout', views.logout, name='logout'),
]
