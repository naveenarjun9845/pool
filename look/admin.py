from django.contrib import admin
from .models import Product, store_name, Order
# Register your models here.
admin.site.register(Product)

admin.site.register(store_name)
admin.site.register(Order)