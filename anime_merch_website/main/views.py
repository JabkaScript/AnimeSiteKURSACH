from django.shortcuts import render
from .models import Categories, Products, Images
from django.template.defaulttags import register


@register.filter
def get_preview(images):
    return images.select_related().values()[0]['preview']


@register.filter
def get_item(dict, key):
    return dict[key]


def index(request):
    return render(request, 'index.html', {'categories': Categories.objects.all(), 'products': Products.objects.all(),
                                          'p_images': Images.objects.all()})


def contact_us(request):
    return render(request, 'contact-us.html')


def cart(request):
    return render(request, 'cart.html')


def not_found(request):
    return render(request, '404.html')


def product_details(request, id):
    return render(request, 'product-details.html', {'prod_info': Products.objects.all().values()[id - 1],
                                                    'p_images': Images.objects.all()})


def login(request):
    return render(request, 'login.html')
