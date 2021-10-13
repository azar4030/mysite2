from django.shortcuts import render, render_to_response
from home.models import Slider, About, Category, Product, Gallery, Customer
from django.http import Http404, JsonResponse, HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    about = About.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    gallerys = Gallery.objects.all()
    customers = Customer.objects.all()
    context = {'sliders': sliders, 'about': about, 'categories': categories, 'products': products, 'gallerys': gallerys,
               'customers': customers}
    return render(request, 'home/home.html', context)


def product(request, id):
    categories = Category.objects.filter(id=id)
    if len(categories) > 0:
        products = Product.objects.filter(category=categories[0].id)
        context = {'categories': categories, 'products': products}
        return render(request, 'home/menu.html', context)
    else:
        raise Http404


def cart_add(request, product_id):
    count = 1
    message = 'Error'
    if 'count' in request.GET:

        if int(request.GET['count']) > 0:
            count = int(request.GET['count'])
    else:
        count = 1

    if len(Product.objects.filter(id=product_id)) > 0:
        product = Product.objects.get(id=product_id)
        price = product.price
        if 'cart' in request.session:
            new_cart = []
            state = False

            for cart in request.session['cart']:
                if product_id == cart['product_id']:
                    state = True
                    cart['count'] = cart['count'] + count
                    cart['price'] = int(cart['one_price']) * int(cart['count'])

                    message = "به سبد خرید اضافه شد!"
                    new_cart.append(cart)
                # else:
                #     message = "موجود نیست"

            if state is False:
                message = "به سبد خرید اضافه شد"

                total_price = int(price) * int(count)
                new_cart.append({'count': count, 'price': total_price, 'one_price': price, 'product_id': product_id})

            request.session['cart'] = new_cart

        else:
            total_price = int(price) * int(count)
            request.session['cart'] = [
                {'count': count, 'price': total_price, 'one_price': price, 'product_id': product_id}]
            message = "به سبد خرید اضافه شد!"

    return JsonResponse({'message': message})

    carts = []
    cart_counter = 0
    total_price = 0
    if 'cart' in request.session:
        for cart in request.session['cart']:
            cart_counter += 1
            total_price += cart['price']
            carts.append(cart)
            product = Product.objects.get(id=cart['product_id'])
            item = {'product': product, 'price': cart['price']}
            carts.append(item)

    context = {'carts': carts, 'total_price': total_price, 'cart_counter': cart_counter}

    template = render_to_string('home/cart.html', context)
    return JsonResponse({'message': message, 'template': template})


def show_cart(request):
    return HttpResponse(str(request.session['cart']))
