from django.db import models
class food1(models.Model):
    name=models.CharField(max_length=255, verbose_name="Название")
    slug=models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")
    photo=models.ImageField(upload_to="Img/", verbose_name='Фото')
    description=models.TextField(verbose_name="Описание")
    price=models.DecimalField(decimal_places=2, max_digits=10,  verbose_name="Цена", default=0)
    weight=models.CharField(max_length=255, verbose_name="Вес")