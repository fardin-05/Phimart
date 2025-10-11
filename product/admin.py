from django.contrib import admin
from .models import Product,Category
class ProductAdmin(admin.ModelAdmin):
    model=Product
    fields=['name','description','price','stock','images','category','created_at','updated_at']
class CategoryAdmin(admin.ModelAdmin):
    model=Category
    fields=['name','description']
admin.site.register(Product)
admin.site.register(Category)

