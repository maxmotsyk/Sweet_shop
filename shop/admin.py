from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Advertisement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'image_show', 'price', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}

    # Show image in django admin panel
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Image"


@admin.register(Advertisement)
class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ('id', 'advertisment_img', 'created_at')
    list_display_links = ('id',)
    list_editable = ('advertisment_img',)

    # Show image in django admin panel
    def advertisment_img(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='100' />".format(obj.image.url))
        return "None"

    advertisment_img.__name__ = "Image"
