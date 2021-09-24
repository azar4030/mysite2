from django.contrib import admin
from home.models import Slider,About,Category,Product,Gallery,GalleryAbout,Customer,Socials
# Register your models here.
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(GalleryAbout)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Gallery)
admin.site.register(Customer)
# admin.site.register(Social)
admin.site.register(Socials)
