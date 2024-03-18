from django.urls import include, path

from . import views

urlpatterns = [
    path('activity/', views.dashboard, name='activity'),
]
