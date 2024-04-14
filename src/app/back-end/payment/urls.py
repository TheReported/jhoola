from django.urls import path

from booking import views

app_name = 'payment'
urlpatterns = [
    path('completed/<int:booking_id>/', views.payment_success, name='payment_completed'),
    path('cancelled/<int:booking_id>/', views.payment_cancel, name='payment_cancelled'),
]
