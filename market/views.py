from django.shortcuts import render, redirect
from .models import Product, Order, ShipingAdress, Customer, Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'market/home.html', context)
@login_required
def add(request, product_id):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer)
    product = Product.objects.get(pk=product_id)
    item, created = Item.objects.get_or_create(order=order, product=product)
    
    item.save()
    messages.success(request, f'Succesfully Added')
    return redirect('home')

@login_required
def remove(request, product_id): 
      customer = request.user.customer 
      order, created = Order.objects.get_or_create(customer=customer)
      product = Product.objects.get(pk=product_id)
      item, created = Item.objects.get_or_create(order=order, product=product)

      item.delete()
      messages.success(request, f'Succesfully deleted')
      return redirect('cart')



@login_required
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer)
    items = order.item_set.all()
    total = sum([item.product.price for item in items])
    context = {
        'items':items,
        'total':total
    }
    return render(request, 'market/cart.html', context)
@login_required
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer)
    items = order.item_set.all()
    total = sum([item.product.price for item in items])
    context = {
        'items':items,
        'total':total
    }
    return render(request, 'market/checkout.html', context)

login_required
def shipment(request):
    customer = request.user.customer
    order = Order.objects.get(customer=customer)
    if request.method == 'POST':
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']

    Shiping = ShipingAdress(customer=customer, order=order, address=address, city=city, state=state)

    Shiping.save()



    return redirect('home')    
