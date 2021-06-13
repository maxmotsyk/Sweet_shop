from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', catalog, name="catalog"),
    path('cart', cart, name="cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

