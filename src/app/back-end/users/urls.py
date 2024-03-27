from django.urls import include, path

from . import views

urlpatterns = [
    path('login/<slug:hotel_slug>/', views.user_login, name='login')
]
