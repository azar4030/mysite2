"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home , product ,cart_add,show_cart

urlpatterns = [

    path('',home,name='home'),
    path('products/<int:id>',product,name='product'),
    path('products/cart/add/<int:product_id>',cart_add, name='cart.add'),
    path('products/show/cart',show_cart,name='show_cart')
    # path('category/<int : id>',category ,name='category_id'),
]
