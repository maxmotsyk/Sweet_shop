from django.shortcuts import render

from .models import Product


def index(request):
    products_sort = Product.objects.all()[:4]
    products = Product.objects.all()
    context = {
        "product_sort" : products_sort,
        "product" : products,
     }
    return render(request, 'main/index.html', context)



