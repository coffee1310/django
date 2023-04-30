from django.contrib import admin

# Register your models here.
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug":('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat')
    list_display_links = ('cat',)
    search_fields = ('cat',)
    prepopulated_fields = {"slug":('cat',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'adress', 'customer_name', 'customer_phone', 'comments', 'status','created')
    list_display_links = ('adress', 'customer_name', 'customer_phone', 'comments', 'status')
    search_fields = ('cat',)



admin.site.register(food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
