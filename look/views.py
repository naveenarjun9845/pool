from django.shortcuts import render, redirect
from look.models import Product,store_name, Order, OrderUpdate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from look.cart import *
import json
from django.http import JsonResponse



    # Create your views here.
def index(request):
    pro = Product.objects.all()
    return render(request, 'index.html', {'pro':pro})

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="admin")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="admin")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="admin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="admin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="admin")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def checkout(request):
    if request.method == 'POST':
        user = request.user
        items_json = request.session.get('cart')
        rud = Order(items_json=items_json, user=user)
        rud.save()
        update = OrderUpdate(order_id=rud.order_id, update_desc="The order has been placed")
        update.save()
    else:
        print('error')
    return render(request, 'cart/checkout.html')

def orders(request):
    order =  Order.objects.filter(user = request.user).order_by('items_json')
    for orderz in order:
        parsed = orderz.items_json
    return render(request, 'order.html', {'parsed':parsed})


