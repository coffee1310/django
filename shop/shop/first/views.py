from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import *
from .forms import *
from .sms import send_message, order
from cart.cart import *
import time

info = [
    {'title': 'Москва'},
    {'title': 'Бесплатная доставка'},
    {'title': '24 часа в сутки'},
]
menu = [
    {'title': 'Контакты', 'url': 'interier','id':9},
    {'title':'О нас', 'url':'AboutUs','id':10}
]
menu_not_home_page = [
    {'title': 'Пицца', 'url': 'home','id':1},
    {'title': 'Суши', 'url': 'home','id':2},
    {'title': 'Напитки', 'url': 'home','id':3},
    {'title': 'Комбо', 'url': 'home','id':4},
    {'title': 'Закуски', 'url': 'home','id':5},
    {'title': 'Десерты', 'url': 'home','id':6},
    {'title': 'Акции', 'url': 'home','id':7},
    {'title': 'Другие товары', 'url': 'home','id':8},
    {'title': 'Контакты', 'url': 'interier','id':9},
    {'title':'О нас', 'url':'AboutUs','id':10}
]


def ShopList(request):
    cat = Category.objects.all()
    posts = food.objects.all()
    print(request)
    return render(request, 'first/index.html', {'menu': menu, 'info': info, 'posts': posts,'request':request,'cat':cat})


def Basket(request):
    posts = food.objects.all()
    context = {
        'info': info,
        'posts': posts,
        'menu_not_home_page':menu_not_home_page
    }
    return render(request, 'first/basket.html', context=context)


def AboutUs(request):
    context = {
        'info': info,
        'menu_not_home_page':menu_not_home_page
    }
    return render(request, 'first/checkout.html', context=context)


def product_detail(request, id, slug):
    product = get_object_or_404(food, id=id, slug=slug, aviable=True)
    return render(request, '', {'product': product, 'cart_product_form': cart_product_form})


def checkout(request):
    if request.method == "POST":
        form = AddOrder(request.POST)
        if form.is_valid():
            form.save()
            order(order_list = [value for key, value in request.session.get("cart", {}).items()],last_order = Order.objects.latest('created'),posts = Order.objects.all())
            return redirect('thanks')
    else:
        form = AddOrder
    return render(request, 'first/to-checkout.html', {'form': form,'info':info,'menu_not_home_page':menu_not_home_page})

def thanks(request):
    cart = Cart(request)
    cart.clear()
    return render(request,'first/thanks.html',{'info':info,'menu_not_home_page':menu_not_home_page})
