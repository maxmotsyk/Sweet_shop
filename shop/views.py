from django.views.generic import ListView
from cart.forms import CartAddProductForm
from .models import Product, Advertisement


class HomeView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'tape/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisment'] = Advertisement.objects.all()[:2]
        context['advertisment_last'] = Advertisement.objects.last()
        context['product_sort'] = Product.objects.all()[:4]
        context['cart_product_form'] = CartAddProductForm()
        return context
