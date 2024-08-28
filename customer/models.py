from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)#ie beverage, electronics,
    brand = models.CharField(max_length=255)#ie apple,  versace, nokia


class Transaction(models.Model):
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    cashier = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now())#today , and time
    payment_method = models.CharField(max_length=255)