from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('manager/bookings/', views.bookings_manager_view, name='manager_bookings'),
    path('manager/products/', views.products_manager_view, name='manager_products'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/users/', views.users_manager_view, name='manager_users'),
    path('manager/products/add', views.products_add_manager_view, name='manager_products_add'),
    path('manager/users/add', views.users_add_manager_view, name='manager_users_add'),
    path(
        'manager/users/<username>/edit/', views.users_edit_manager_view, name='manager_users_edit'
    ),
    path(
        'manager/products/<product_id>/edit/',
        views.products_edit_manager_view,
        name='manager_products_edit',
    ),
    path(
        'manager/users/<username>/delete/',
        views.users_delete_manager_view,
        name='manager_users_delete',
    ),
    path(
        'manager/products/<product_id>/delete/',
        views.products_delete_manager_view,
        name='manager_products_delete',
    ),
    path(
        'manager/bookings/<booking_id>/delete/',
        views.bookings_delete_manager_view,
        name='manager_bookings_delete',
    ),
    path(
        'manager/search/',
        views.search_manager_view,
        name='manager_search',
    ),
    path(
        'manager/check_booking/',
        views.check_booking_manager_view,
        name='manager_check_booking',
    ),
]
