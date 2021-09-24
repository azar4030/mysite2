from django.shortcuts import render
from home.models import Slider,About,Category,Product,Gallery,Customer


# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    about = About.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    gallerys = Gallery.objects.all()
    customers = Customer.objects.all()
    context = {'sliders': sliders, 'about':about,'categories':categories,'products':products,'gallerys':gallerys ,'customers':customers}
    return render(request, 'home/home.html', context)

# def category(request ,id ):
#     categories = Category.objects.get(id=id)
#     return render(request,'home/home.html',categories)