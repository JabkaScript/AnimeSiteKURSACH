from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def cart(request):
    return render(request, 'cart.html')
