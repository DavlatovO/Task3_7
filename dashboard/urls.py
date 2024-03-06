from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('banner-list/', views.list_banner),
    path('banner-create/', views.create_banner),
    path('aboutus-list/', views.list_aboutus ),
    path('aboutus-create/', views.create_aboutus),
    path('service-create/', views.create_service),
    path('service-list/', views.list_service),

]