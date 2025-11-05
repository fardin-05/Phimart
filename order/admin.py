from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem
#id Show in Admin Site
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','status']
#Item Show in Admin Site
admin.site.register(CartItem)
admin.site.register(OrderItem)

