from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()
    baner = models.Banner.objects.last()
    about_us = models.AboutUs.objects.last()
    services = models.Service.objects.all()

    context = {
        'contacts':contacts,
        'baner':baner,
        'about_us':about_us,
        'service':services

    }
    return render(request, 'front/index.html', context)

def about_us(request):
    about_us = models.AboutUs.objects.all()
    context = {
        'about_us': about_us
    }
    return render(request, 'front/about.html', context)


def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'front/contact.html')

prices_list = []
def price(request):
     for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

     context = {
         'price':prices_list
     }   
     return render(request, 'front/price.html', context) 