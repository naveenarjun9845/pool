from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class store_name(models.Model):
    Store = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.Store

class Product(models.Model):
    des = models.CharField(max_length=200, default='')
    store = models.CharField(default='', max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics', blank=True)

class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=100000)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
