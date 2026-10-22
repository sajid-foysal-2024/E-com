from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart,name='cart'),
    path('cart_add/<int:product_id>/',views.cart_add,name='cart_add'),
    path('remove_cart/<int:product_id>/',views.remove_cart,name='remove_cart'),
    path('remove_cart_item/<int:cart_id>/',views.remove_cart_item,name='remove_cart_item'),


    
]

