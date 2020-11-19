from django.contrib.sitemaps.views import index
from django.urls import path
from . import views
from django.urls import *
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("",views.ProductsView.as_view(), name="index_page"),
    path("<slug:slug>/",views.ProductDetailView.as_view(),name='product_detail_url'),
    path("review/<int:pk>/",views.AddReview.as_view(),name='add_review'),
    path("our_products", ProductsPage,name="all_products_url"),
    path("about_us",about_us,name="about_url"),
    path("contacts",views.contacts_page.as_view(),name="contacts_url"),
    path("price/20",views.price_page.as_view(),name="price_20_url"),
    path("price/40",views.price_page_40.as_view(),name="price_40_url"),
    path("modern_tendence",views.modern_tendence_page.as_view(),name="modern_url"),
    path("brand",views.brand_page.as_view(),name="brand_url")
    # path("about/",AboutView,name="about_us")

]