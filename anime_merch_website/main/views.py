from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories, Products, Images, Orders, Ordersproducts, Status, Clients
from django.template.defaulttags import register
from .cart import Cart


# Ситуация вообще забавная, но objects != objects.values() - иногда требуется именно второе
@register.filter
def get_item(dict, key):
    return getattr(dict, key)


@register.filter
def get_item_from_values(dict, key):
    return dict[key]


@register.filter
def addstr(str1, str2):
    return str1 + str(str2)


def index(request):
    category_id = request.GET.get('category')
    category_id = category_id if category_id is not None else '0'

    if request.method == 'POST':
        cart = Cart(request)
        cart.add(request.POST.get('id'), 1)
        request.session.modified = True

    return render(request, 'index.html', {'categories': Categories.objects.all(),
                                          'products': Products.objects.filter(
                                              cat=category_id) if category_id != '0' else Products.objects.all(),
                                          'p_images': Images.objects.all()})


def contact_us(request):
    return render(request, 'contact-us.html')


def check_it_out(request):
    return render(request, 'check_out.html')


def coca_cola_pizza_confirm(request, address, commentary):
    if request.method == 'POST':
        Orders.objects.create(order_id=len(Orders.objects.all()) + 1, status=Status.objects.all()[0],
                              client=Clients.objects.all()[0], address=address, comment=commentary)
        cart = Cart(request)
        cart.clear()
        request.session.modified = True
    return HttpResponse('Success')


def cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        quantity = int(quantity) if int(quantity) else 1
        cart.add(product_id, quantity)
        request.session.modified = True

    return render(request, 'cart.html', {'products': Cart(request)})


def get_quantity(request, product_id):
    cart = Cart(request)
    return HttpResponse(cart.quantity(product_id))


def not_found(request):
    return render(request, '404.html')


def product_details(request, id):
    return render(request, 'product_details.html', {'prod_info': Products.objects.all()[id - 1],
                                                    'p_images': Images.objects.all(), 'desc_img_count': range(1, 4)})


def login(request):
    return render(request, 'login.html')
