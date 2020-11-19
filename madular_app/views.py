
from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
from .forms import ReviewForm
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View
from django.urls import reverse

from django.shortcuts import get_object_or_404
from .utils import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q
from .utils import *




class ProductsView(ListView):
    "весь ассортимент товаров"
    def get(self,request):
        products =  Products.objects.filter(draft=False)
        return render(request,"index.html",{"products_list":products})


class ProductDetailView(DetailView):
    """Страница товаров"""
    def get(self,request,slug):
        products = Products.objects.get(url=slug)
        return render(request,'product/product.html',{'products':products})

class AddReview(View):
    """Отправка отзывов"""
    def post(self,request,pk):
        form = ReviewForm(request.POST) #Все данные из HTML из фронта
        product = Products.objects.get(id=pk) #Получаем продукт с таким айди 
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


def ProductsPage(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Products.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        products = Products.objects.all()
    return render(request,"product/all_products.html",{"products_list":products})


def about_us(request):
    return render(request,"about.html")



class contacts_page(ListView):
    "весь ассортимент сварочной работы"
    def get(self,request):
        return render(request,"contact.html")


class price_page(ListView):
    "весь ассортимент сварочной работы"
    def get(self,request):
        return render(request,"price.html")

class price_page_40(ListView):
    "весь ассортимент сварочной работы"
    def get(self,request):
        return render(request,"price-big.html")

class modern_tendence_page(ListView):
    "весь ассортимент сварочной работы"
    def get(self,request):
        return render(request,"modern.html")

class brand_page(ListView):
    "весь ассортимент сварочной работы"
    def get(self,request):
        return render(request,"brand.html")