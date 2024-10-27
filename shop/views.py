from django.shortcuts import render
from shop.models import Product


# Create your views here.

def cotalogggggg(request):
    products = Product.objects.all()
    return render(request, 'shop/cotalogggggg.html', {'products': products})

def orders(request):
    return render(request, 'shop/orders.html')

def create_order(request):
    return render(request, 'shop/create_order.html')

def product_detail(request):
    return render(request, 'shop/product_detail.html')