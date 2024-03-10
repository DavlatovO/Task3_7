from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about_us),
    path('contact', views.contact),
    path('price', views.price),

]    