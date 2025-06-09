from django.urls import path
from . import views

urlpatterns = [
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    path('vendor/register/success/', views.vendor_register_success, name='vendor_register_success'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/service/add/', views.add_service, name='add_service'),
    path('customer/register/', views.customer_register, name='customer_register'),
]
