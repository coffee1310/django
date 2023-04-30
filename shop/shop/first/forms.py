from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import forms
from .models import *
from django import forms
from django.core.exceptions import *
class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["adress", "customer_name", "customer_phone", "comments", "email"]
        widgets = {
            'adress':forms.TextInput(attrs={"class":"adress"}),
            'customer_name':forms.TextInput(attrs={"class":"customer-name"}),
            'customer_phone':forms.TextInput(attrs={"class":"phone","type":"tel", "id":"phone"}),
            'email':forms.EmailInput(attrs={"class":"customer-email"}),
            'comments':forms.Textarea(attrs={"class":"comments",})

        }