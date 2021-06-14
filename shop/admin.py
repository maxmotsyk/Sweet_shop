from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category' ,'image', 'price', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_editable = ('is_published', )


admin.site.register(Product, ProductAdmin)


