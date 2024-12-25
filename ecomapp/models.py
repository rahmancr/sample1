from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customer_register (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    mobile_number = models.CharField(max_length=15)
    history = models.TextField(blank=True)

    def __str__(self):
        return self.username
class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    def __str__(self):
        return self.username

class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.productname

