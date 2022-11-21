from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('airtime-topup/', views.airtime_topup, name='airtime_topup'),
    path('data-topup/', views.data_topup, name='data_topup'),
    path('airtime_history/', views.airtime_history, name='airtime_history'),
]