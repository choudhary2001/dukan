from django.contrib import admin
from .models import Category, Product, Banner

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')
admin.site.register(Category,CategoryAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')
admin.site.register(Banner, BannerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id',  'title', 'size', 'weight', 'image_tag',  'quantity' , 'price',  'is_featured')
    list_editable=('is_featured',)
admin.site.register(Product,ProductAdmin)

