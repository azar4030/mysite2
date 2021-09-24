
from django import template
from django.urls import reverse
from .models import Socials

register = template.Library()

@register.simple_tag
def social():
    social = Socials.objects.all()
    return social