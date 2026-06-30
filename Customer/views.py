from django.shortcuts import render,redirect 
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home.html")
def product(request):
    return render(request,"product.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def idols(request):
    return render(request,"idols.html")
def register(request):
    if request.method=="POST":
        fn=request.POST['fname']
        un=request.POST['uname']
        em=request.POST['email']
        p1=request.POST['pass']
        p2=request.POST['pass1']
        if p1==p2:
            if User.objects.filter(username=un).exists():
                 messages.info(request,"Username.Exists")
                 return render(request,"register.html")
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                 user=User.objects.create_user(first_name=fn,email=em,password=p2,username=un)
                 user.save()
                 return HttpResponseRedirect('login.html')
        else:
            messages.info(request,"Password not matching")  
            return render(request,"register.html")  
    else:
        return render(request,"register.html")
    return render(request,"register.html")
def deepa(request):
    return render(request,"deepa.html")
def bells(request):
    return render(request,"bells.html")
def cart(request):
    return render(request,"cart.html")
def login(request):
    if request.method=="POST":
        un=request.POST['uname']
        p1=request.POST['pass']
        user=auth.authenticate(username=un,password=p1)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('home.html')
        else:
            messages.info(request,"Invalid crendentials")
            return render(request,"login.html")
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('home.html')