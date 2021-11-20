from django.db import models
from django.db.models.fields import related
from main.models import User
from product.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=100)
    state = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    block = models.CharField(max_length=50)
    post_office = models.CharField(max_length=60)
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    user_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return '%s' % self.id