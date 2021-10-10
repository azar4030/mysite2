from django.shortcuts import render
from django import template
from django.http import Http404,HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Socials, Category, Product

register = template.Library()


@register.simple_tag
def social():
    social = Socials.objects.all()
    return social


@register.simple_tag
def product(request, id=0):
    if id == 0:
         first_category = Category.objects.first()
         categories = Category.objects.all()
    else:

        first_category = Category.objects.get(id=id)
        categories = Category.objects.all()
    if len(categories) > 0:
        products = Product.objects.filter(category=first_category.id)
        context = {'categories': categories, 'products': products}
        return render_to_string('home/main _menu.html',context,request)
    else:
        raise Http404
