from django.shortcuts import render
from .models import Product

def catalog(request):
    product = Product.objects.all()
    context = {"product" : product}
    return render(request, 'main/catalog/products.html', context)


def cart(request):
    return render(request, 'main/cart/cart.html')


