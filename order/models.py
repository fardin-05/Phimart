from django.db import models
from users.models import User
from product.models import Product
class Cart(models.Model):
    user=models.OneToOneField(
        User, on_delete= models.CASCADE,
        related_name='cart')
    createad_at= models.DateTimeField(  auto_now_add=True)

    def __str__(self):
        return f"Cart Of {self.user.username}"
class CartItem(models.Model):
    cart=models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='item')
    product=models.ForeignKey(
        Product, on_delete=models.CASCADE )
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
class Order(models.Model):
    PENDING='pending'
    SHIPPED='shipped'
    DELIVERED='delivered'
    STATUS_CHOICES=[
        (PENDING,'pending'),
        (SHIPPED,'shipped'),
        (DELIVERED,'delivered'),
    ]
    user=models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='orders')
    status=models.CharField(max_length=200, choices=STATUS_CHOICES, default=PENDING)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order{self.id} By {self.user.username}"
class OrderItem(models.Model):
    order=models.ForeignKey(
        Order,on_delete=models.CASCADE,
        related_name='items')
    product=models.ForeignKey(
        Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}' 


