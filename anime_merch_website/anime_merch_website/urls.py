from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us', views.contact_us, name='contact_us'),
    path('', views.index, name='home')
]
