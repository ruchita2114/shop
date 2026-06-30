from django.urls import path
from .import views

urlpatterns=[
    path('home.html',views.home,name='customerhome'),
    path('product.html',views.product,name='productpage'),
    path('about.html',views.about,name='aboutpage'),
    path('contact.html',views.contact,name='contactpage'),
    path('login.html',views.login,name='loginpage'),
    path('register.html',views.register,name='registerpage'),
    path('deepa.html',views.deepa,name='deepapage'),
    path('bells.html',views.deepa,name='bellspage'),
    path('logout.html',views.logout,name='logoutpage'),
    path('idols.html',views.idols,name='idolspage'),
    path('cart.html',views.cart,name='cartpage'),
]