from django.shortcuts import render
from .models import Product
 

def catalog(request):
    product_sort = Product.objects.all()[:4]
    product = Product.objects.all()
    context = {
        "product_sort" : product_sort,
        "product" : product,
     }
    return render(request, 'main/catalog/products.html', context)


def cart(request):
    return render(request, 'main/cart/cart.html')


