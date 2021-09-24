from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.contrib.admin.forms import forms
# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='public/slider/img')
    alt = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class About(models.Model):
    Text = RichTextField()
    # Text = models.TextField()
    # img = models.ImageField(upload_to='public/about/img')


class GalleryAbout(models.Model):
    img = models.ImageField(upload_to='public/img/galleries')
    name = models.CharField(max_length=250)

class Category(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='public/product/img')
    price = models.CharField(max_length=250)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    alt = models.CharField(max_length=250)
    img = models.ImageField(upload_to='public/gallery/img')

class Customer(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='public/customer/img')
    text = RichTextField()

    def __str__(self):
        return self.name
# class Social(models.Model):
#     name = models.CharField(max_length=250)
#     link = models.CharField(max_length=250)
#     img = models.ImageField(upload_to='public/social/img')

class Socials(models.Model):
    link = models.CharField(max_length=250)
    img = models.ImageField(upload_to='public/social/img')


