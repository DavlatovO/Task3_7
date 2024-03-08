from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('banner-list/', views.list_banner),
    path('banner-create/', views.create_banner),
    path('banner-detail/<int:id>/', views.banner_detail, name='banner_detail'),
    path('banner-edit/<int:id>/', views.banner_edit, name='banner_edit'),
    path('banner-delete/<int:id>/', views.banner_delete, name='banner_delete'),
    path('aboutus-list/', views.list_aboutus ),
    path('aboutus-create/', views.create_aboutus),
    path('aboutus-detail/<int:id>/', views.aboutus_detail, name='aboutus-detail'),
    path('aboutus-edit/<int:id>/', views.aboutus_edit, name='aboutus_edit'),
    path('aboutus-delete/<int:id>/', views.aboutus_delete, name='aboutus_delete'),
    path('service-create/', views.create_service),
    path('service-list/', views.list_service),
    path('service-detail/<int:id>/', views.service_detail, name='service_detail'),
    path('service-edit/<int:id>/', views.service_edit, name='service_edit'),
    path('service-delete/<int:id>/', views.service_delete, name='service_delete'),
     
]