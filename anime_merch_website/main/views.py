from django.shortcuts import render
from .models import Categories, Products, Images
from django.template.defaulttags import register


@register.filter
def get_item(dict, key):
    return getattr(dict, key)


@register.filter
def addstr(str1, str2):
    return str1 + str(str2)


def index(request):
    return render(request, 'index.html', {'categories': Categories.objects.all(), 'products': Products.objects.all(),
                                          'p_images': Images.objects.all(), 'aboba': range(40)})


def contact_us(request):
    return render(request, 'contact-us.html')


def cart(request):
    return render(request, 'cart.html')


def not_found(request):
    return render(request, '404.html')


def product_details(request, id):
    return render(request, 'product_details.html', {'prod_info': Products.objects.all()[id - 1],
                                                    'p_images': Images.objects.all(), 'desc_img_count': range(1, 4)})


def login(request):
    return render(request, 'login.html')
