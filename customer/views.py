from django.shortcuts import render, redirect
from .models import Product
from .models import Transaction

# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    allproducts = Product.objects.all()
    context ={
        'allproducts':allproducts
    }
    return render(request, 'home.html', context )


def search_product(request):
    if request.method=='POST':
        searched_product = request.POST['searched_product']
        results = Product.objects.filter(product_contains=searched_product)
        return render(request, 'searched_product.html', {'results':results})
    

def add_product(request):
    if request.method=='POST':
        name = request.POST['name']
        image = request.POST['image']
        price = request.POST['price']
        description = request.POST['description']
        quantity = request.POST['quantity']
        category = request.POST ['category']
        brand = request.POST['brand']

        new_product = Product()
        new_product.name = name
        new_product.image = image
        new_product.price = price
        new_product.description = description
        new_product.quantity = quantity
        new_product.category = category
        new_product.brand = brand
        new_product.save()
        return redirect('/home/')
    return render(request, 'add_product.html')


def invoice(request):
    
    return render(request, 'invoice.html')


def receipts(request):

    return render(request, 'receipts.html')


def view_product(request, id):
        product = Product.objects.get(id=id)
        context = {
           'product': product
        }

        return render(request, 'view_product.html', context)  


def buy_product(request):
    return render(request, 'buy_product.html')


def invoice(request, id):
    invoice = Product.objects.get(id=id)
    context = {
        'invoice':invoice
    }
    return render(request, 'invoice.html', context)