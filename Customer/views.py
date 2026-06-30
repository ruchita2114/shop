from django.shortcuts import render

def home(request):
    return render(request, "customer/home.html")

def product(request):
    return render(request, "customer/product.html")

def about(request):
    return render(request, "customer/about.html")

def contact(request):
    return render(request, "customer/contact.html")