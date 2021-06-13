from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name="Имя категории")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Названия', blank=False)
    image = models.ImageField(verbose_name='Изображения', upload_to="cake_image", default="cake_image/err.png")
    description = models.CharField(max_length=255, verbose_name='Описание', blank=False)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Создано")
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'


# class Customer(models.Model):

#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#     phone = models.CharField(max_length=25, verbose_name='Номер телефона')
#     address = models.CharField(max_length=255, verbose_name='Адрес')

#     def __str__(self):
#         return f'Покупатель : {self.user.first_name}, {self.user.last_name}'

