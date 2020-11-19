from django.db import models
from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Имя",max_length=150)
    desctiption = models.TextField("Описание")
    url = models.SlugField(max_length=150,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Products(models.Model):
    name = models.CharField("Имя",max_length = 100)
    cash = models.CharField("Цена",max_length = 30)
    width = models.CharField("Размеры",max_length = 30)
    height = models.CharField("Высота", max_length = 30)
    weight = models.CharField("Вес", max_length = 30)
    description = models.TextField("Описание")
    picture = models.ImageField("Картинка",upload_to='')
    draft = models.BooleanField("Черновик",default=False)
    category = models.ManyToManyField(Category, verbose_name="Категории")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class PageShots(models.Model):
    title = models.CharField("Заголовок",max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='pictures_detail/')
    product = models.ForeignKey(Products,verbose_name="Товар",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Картинка в странице"
        verbose_name_plural = "Картинки в страницах"

class Reviews(models.Model):
    name = models.CharField("Имя",max_length=100)
    number = models.CharField("Номер телефона", max_length=30)
    text = models.TextField("Сообщение",max_length=5000)
    parent = models.ForeignKey(
        'self',verbose_name="Родитель",on_delete=models.SET_NULL,blank=True,null=True
    )
    product = models.ForeignKey(Products,verbose_name="товар",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"