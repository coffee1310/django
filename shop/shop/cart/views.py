from django.shortcuts import render, redirect
from first.models import food
from django.contrib.auth.decorators import login_required
from .cart import Cart

info=[
    {'title':'Москва'},
    {'title':'Бесплатная доставка'},
    {'title':'24 часа в сутки'},
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


def cart_add(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


def cart_decrement(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("home")


def item_clear(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    context = {'info':info,
               'menu_not_home_page':menu_not_home_page,
               }
    return render(request, 'cart/detail.html',context=context)


def count_add(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.count_add(product=product)
    return redirect("home")


def count_decrement(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.count_decrement(product=product)
    return redirect("home")
@login_required(login_url="/users/login")
def count_length(request, id):
    cart = Cart(request)
    product = food.objects.get(id=id)
    cart.count_length(product=product)
    return redirect("home")
