from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login/<slug:hotel_slug>/', views.user_login, name='login'),
    path('dashboard/<slug:hotel_slug>/', views.dashboard, name='dashboard'),
]
