from django.shortcuts import render
from menu.models import Slider
from home.models import Customer
from django.http import Http404
from home.views import product

# Create your views here.

def menu(request):
    sliders = Slider.objects.all()
    customer = Customer.objects.all()
    context = {'sliders': sliders,'customer':customer}
    return render(request, 'menu/menu.html', context)



    




