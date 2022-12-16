from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us', views.contact_us, name='contact_us'),
    path('cart', views.cart, name='cart'),
    path('404', views.not_found, name='404'),
    path('product/<int:id>', views.product_details, name='product'),
    path('login', views.login, name='login'),
    path('quantity/<int:product_id>', views.get_quantity, name='quantity'),
    path('checkout', views.check_it_out, name='checkout'),
    path('confirm_order/<str:address>&<str:commentary>', views.coca_cola_pizza_confirm, name='confirm_order'),
    path('', views.index, name='home'),
]
