
from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from first.models import *
import copy

class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.id
        if len(self.cart.items()) == 0:
            self.cart = {'0':{'userid':0, 'product_id':0,'name':'','quantity':0,'count':0,'price':'0','photo':'None'}}
        newItem = True
        cart_copy = self.cart.copy()
        if str(product.id) not in self.cart.keys():
            for key, value in cart_copy.items():
                    self.cart[product.id] = {
                        'userid': self.request.user.id,
                        'product_id': id,
                        'name': product.name,
                        'quantity': 1,
                        'count':1,
                        'price': str(product.price),
                        'photo': product.photo.url
                    }
            print(cart_copy)
        else:
            newItem = True
            for key, value in self.cart.items():
                if key == str(product.id):

                    value['quantity'] =value['quantity'] + value['count']
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    'image': product.image.url
                }
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def count_add(self,product, quantity=1, action=None, count=1):
        """
         Add a product to the cart or update its quantity.
        """
        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():
                    self.cart[product.id] = {
                        'userid': self.request.user.id,
                        'product_id': id,
                        'name': product.name,
                        'count':2,
                        'quantity': 0,
                        'price': str(product.price),
                        'photo': product.photo.url
                    }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    value['count'] = value['count'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:
                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 2,
                    'price': str(product.price),
                    'image': product.image.url
                }

        self.save()
    def count_decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['count'] = value['count'] - 1
                if(value['count'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")
    def count_length(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                if product.id == food.objects.filter(id=product.id):
                    return value[product.id]
                break



