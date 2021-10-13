from django.shortcuts import render
from contact.models import Slider
# Create your views here.

def contact(request):
    slider = Slider.objects.all()
    context = {'slider':slider}
    return render(request,'contact/contact.html',context)
