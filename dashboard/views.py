from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from functools import wraps
from django.db.models import Q





@login_required(login_url='dashboard:log_in')
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)






# CRUD 

# Create
# Read -> List/Detail
# Update
# Delte

def create_banner(request):
    if request.method == "POST":
       try: 
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
        messages.success(request, "Banner muvaffaqiyatli yaratildi")
       except:
            messages.error(request, "Banner yaratilishda xatolikro'y berdi")
    return render(request, 'dashboard/banner/create.html')


@login_required(login_url='dashboard:log_in')
def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

@login_required(login_url='dashboard:log_in')
def banner_detail(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)

@login_required(login_url='dashboard:log_in')
def banner_edit(request, id):
    banner = models.Banner.objects.get(id=id)

    if request.method == 'POST':
        try:
            banner.title = request.POST['title']
            banner.body = request.POST['body']
            banner.save()
            messages.success(request, "Banner muvaffaqiyatli o'zgartirildi")
            return redirect('banner_detail', banner.id)
        except:
            messages.error(request, "Xatolik ro'y berdi")

    # Move the context definition inside the 'if' block
    context = {
        'banner': banner
    }

    return render(request, 'dashboard/banner/edit.html', context)

@login_required(login_url='dashboard:log_in')
def banner_delete(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('list_banner')


def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            # Create the user
            user = User.objects.create_user(username=username, password=password)

            # Log in the user after successful registration
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

                # Redirect to the desired page after registration and login
                return redirect('dashboard:index')

    return render(request, 'dashboard/auth/register.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            # Add the following line to render the login template with an error message
            return render(request, 'dashboard/auth/login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('dashboard:log_in')

@login_required(login_url='dashboard:log_in')
def create_aboutus(request):
    if request.method == "POST":
       try: 
        body = request.POST['body']
        models.AboutUs.objects.create(
            body = body,
        )
        messages.success(request, "AboutUS muvaffaqiyatli yaratildi")
       except:
        messages.error(request, "Xatolik ro'y berdi")
                 
    return render(request, 'dashboard/aboutus/create.html')

@login_required(login_url='dashboard:log_in')
def aboutus_list(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }    
    return render(request, 'dashboard/aboutus/list.html', context )

@login_required(login_url='dashboard:log_in')
def aboutus_detail(request,id):
    aboutus = models.AboutUs.objects.get(id=id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/detail.html', context)

@login_required(login_url='dashboard:log_in')
def aboutus_edit(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
       try: 
        aboutus.body = request.POST['body']
        aboutus.save()
        messages.success(request, "AboutUS muvaffaqiyatli o'zgartirildi")
       except:
            messages.error(request, "Xatolik ro'y berdi")
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/edit.html', context)

@login_required(login_url='dashboard:log_in')
def aboutus_delete(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('list_aboutus')
    
@login_required(login_url='dashboard:log_in')    
def create_service(request):
    if request.method == "POST":
       try:
        name= request.POST['title']
        body = request.POST['body']
        icon = request.POST['icon']
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon,
        )
        messages.success(request, "Service muvaffaqiyatli yaratildi")
       except:
           messages.error(request, "Xatolik yuz berdi") 
    return render(request, 'dashboard/service/create.html')

@login_required(login_url='dashboard:log_in')
def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }    
    

    return render(request, 'dashboard/service/list.html', context)

@login_required(login_url='dashboard:log_in')
def service_detail(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)

@login_required(login_url='dashboard:log_in')
def service_edit(request, id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
       try: 
        service.name = request.POST['name']
        service.body = request.POST['body']
        service.icon = request.POST['icon']
        messages.success(request, "Servis muvaffaqiyatli o'zgartirildi")
        return redirect( 'service_detail', service.id)
       except:
           messages.error(request, "Xatolik yuz berdi")
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)
    
@login_required(login_url='dashboard:log_in')    
def service_delete(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('list_service')


def query(request):
    q = request.GET.get('q', '')  
    banners = models.Banner.objects.filter(Q(title__icontains=q) | Q(body__icontains=q)) 
    services = models.Service.objects.filter(name__startswith=q)
    prices = models.Price.objects.filter(title__icontains=q)
    contacts = models.Contact.objects.filter(name__icontains=q) 
    context = {
        'banners': banners,
        'services': services,
        'prices': prices,
        'contacts': contacts,
    }
    return render(request, 'dashboard/query.html', context)
