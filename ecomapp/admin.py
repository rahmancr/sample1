from django.contrib import admin

# Register your models here.
from .models import customer_register
admin.site.register(customer_register)
from .models import Product
admin.site.register(Product)