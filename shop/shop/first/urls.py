from django.urls import path, include
from .views import *
from cart.views import *
urlpatterns = [
    path('', ShopList, name="home"),
    path('', ShopList, name="category"),
    path('', ShopList, name="interier"),
    path('basket/', Basket, name='basket'),
    path('about_us/', AboutUs, name='AboutUs'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    path('cart/cart_decrement/<int:id>/', cart_decrement, name='cart_decrement'),
    path('cart/count_add/<int:id>', count_add, name='count_add'),
    path('cart/count_decrement/<int:id>', count_decrement, name='count_decrement'),
    path('cart/count_length/<int:id>', count_length, name="count_length"),
    path('checkout/', checkout, name='checkout'),
    path('thanks/', thanks, name='thanks')
]
