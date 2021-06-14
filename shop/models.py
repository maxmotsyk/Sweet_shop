from django.db import models


class Product(models.Model):


    CAKE = 'Торт'
    CHESS_CAKE = 'Чизкейк'
    MARSHMALLOWS = 'Маршмеллоу'
    CAP_CAKE = 'Капкейки'


    CHOICE_CATEGORY = {
        (CAKE, 'Торт'),
        (CHESS_CAKE, 'Чизкейк'),
        (MARSHMALLOWS, 'Маршмеллоу'),        
        (CAP_CAKE, 'Капкейки'),
    }


    title = models.CharField(max_length=100, verbose_name='Названия', blank=False)
    image = models.ImageField(verbose_name='Изображения', upload_to="cake_image", default="cake_image/err.png")
    description = models.CharField(max_length=150, verbose_name='Описание', blank=False)
    category = models.CharField(max_length=40, verbose_name="Категория", choices=CHOICE_CATEGORY, default=CAKE)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=0)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Создано")
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ["-id"]



