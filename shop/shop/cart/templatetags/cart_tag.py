from django import template
import operator
from first.models import *
register = template.Library()
from cart.cart import *
import operator
@register.filter()
def multiply(value, arg):
    return float(value) * arg

@register.simple_tag()
def count1(id, request):
    post = food.objects.filter(id=id)
    on = 0
    for p in post:
        food_id = p.pk
    order = [value for key, value in request.session.get("cart", {}).items()]
    order_id = []
    for o in order:
        order_id.append(o.get('product_id'))
    result = order_id.count(food_id)
    if result>0:
        for p in order:
            on+=1
            if p.get('product_id') == food_id:
                return order[on-1].get('count')
    else:
        return 1

@register.simple_tag()
def cart_length(request):
    length = 0
    order = [value for key, value in request.session.get("cart", {}).items()]
    for o in order:
        if o.get('quantity') != 0:
            length+=1
    return length

@register.simple_tag()
def food_price(request, id):
    order = [value for key, value in request.session.get("cart", {}).items()]
    post = food.objects.filter(id=id)
    posts = food.objects.all()
    order_list = [o.get('product_id') for o in order]
    def get_data_for_sort(dic):
        return dic['product_id']

    for p in post:
        food_id = p.pk
    for p in posts:
        if p.pk not in order_list:
            order.insert(p.pk-1,{'product_id':p.pk,'count':1,'price':p.price})
    order_sort = sorted(order,key=get_data_for_sort)
    for o in order_sort:
        if o.get('product_id') == food_id:
            return float(o.get('price')) * o.get('count')

@register.simple_tag()
def order_price(request):
    order = [value for key, value in request.session.get("cart", {}).items()]
    order_price = 0
    for o in order:
        price = o.get('price')
        quantity = o.get('quantity')
        order_price += float(price) * float(quantity)
    return order_price