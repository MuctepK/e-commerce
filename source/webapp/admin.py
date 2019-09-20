from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'remain', 'price']
    list_display_links = ['name']
    list_filter = ['category']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'category', 'remain', 'price']


admin.site.register(Product, ProductAdmin)