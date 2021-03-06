from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class Product(models.Model):

    CAKE = 'Cake'
    CHESS_CAKE = 'Chesscake'
    MARSHMALLOWS = 'Marshmello'
    CAP_CAKE = 'Capcake'

    CHOICE_CATEGORY = {
        (CAKE, 'Cake'),
        (CHESS_CAKE, 'Chesscake'),
        (MARSHMALLOWS, 'Marshmello'),        
        (CAP_CAKE, 'Capcake'),
    }

    title = models.CharField(verbose_name='Name', max_length=100, blank=False)
    category = models.CharField(verbose_name="Category", max_length=60, choices=CHOICE_CATEGORY, default=CAKE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image', upload_to="product")
    description = models.CharField(verbose_name='Description', max_length=150, blank=False)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=0, blank=False)
    created_at = models.DateTimeField(verbose_name="Created", auto_now=True, auto_now_add=False)
    is_published = models.BooleanField(verbose_name='Published?', default=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-id", ]

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    name = models.SlugField(verbose_name='Name', max_length=100, blank='True')
    image = models.ImageField(verbose_name='Image', upload_to='advertisment/')
    created_at = models.DateTimeField(verbose_name='Date of published', auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'product_advertisement'

    def __str__(self):
        return self.name



    
