from django.db import models


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
    image = models.ImageField(verbose_name='Image', upload_to="product")
    description = models.CharField( verbose_name='Description', max_length=150, blank=False)
    category = models.CharField(verbose_name="Category", max_length=40, choices=CHOICE_CATEGORY, default=CAKE)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=0, blank=False)
    created_at = models.DateTimeField(verbose_name="Created", auto_now=True, auto_now_add=False)
    is_published = models.BooleanField(verbose_name='Published?', default=True)


    def __str__(self):
        return self.title

    
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-id",]



