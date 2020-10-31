from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add/<int:product_id>', views.add, name='add'),
    path('remove/<int:product_id>', views.remove, name='remove'),
    path('paid/', views.shipment, name='shipment'),
    
    
]