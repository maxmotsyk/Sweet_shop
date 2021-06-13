from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('title', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


