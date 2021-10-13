from django.shortcuts import render
from about.models import Slider
from home.models import About
# Create your views here.

def about(request):
    sliders = Slider.objects.all()
    abouts = About.objects.first()
    context = {'sliders': sliders,'abouts':abouts}
    return render(request, 'about/about.html', context)
