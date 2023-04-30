from django.db import models
# Create your models here.
from django.db.models import options
from phonenumber_field.modelfields import PhoneNumberField


class food(models.Model):
    name=models.CharField(max_length=255, verbose_name="Название")
    slug=models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")
    photo=models.ImageField(upload_to="Img/", verbose_name='Фото')
    description=models.TextField(verbose_name="Описание", blank=True,)
    price=models.DecimalField(decimal_places=2, max_digits=10,  verbose_name="Цена", default=0)
    weight=models.CharField(max_length=255, verbose_name="Вес", blank=True)
    cat=models.ForeignKey('Category', models.DO_NOTHING)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name='Еда'
        verbose_name_plural='Еда'



class Category(models.Model):
    cat=models.CharField(max_length=255, verbose_name="Категория")
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.cat

    class Meta():
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Order(models.Model):
    adress=models.CharField(max_length=256, null=True, default=None, verbose_name = "Адрес")
    email=models.EmailField(max_length=254,blank=False, default=None, verbose_name="Email")
    customer_name=models.CharField(max_length=64, null=True, default=None, verbose_name = "Ваше имя")
    customer_phone=PhoneNumberField(max_length=48, null=False, default=None, verbose_name = "Номер телефона")
    comments=models.TextField(blank=True, null=True, default=None, verbose_name = "Комментарий к заказу")
    status=models.BooleanField(default=True, verbose_name="Активно")
    created=models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Заказ %s" % self.id

    class Meta:
        verbose_name="Заказ"
        verbose_name_plural="Заказ"
