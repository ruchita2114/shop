from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home is working")

def product(request):
    return render(request, "customer/product.html")

def about(request):
    return render(request, "customer/about.html")

def contact(request):
    return render(request, "customer/contact.html")

def cart(request):
    return render(request, "cart.html")

def logout(request):
    return render(request, "customer/login.html")