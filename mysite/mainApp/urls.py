from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    #url('product/(?P<product_id>\w+)/', views.product, name='product'),
    url('', views.home, name='home'),
    url('basket_adding/', views.basket_adding, name='basket_adding'),
    url('checkout/', views.checkout, name='checkout'),
]
