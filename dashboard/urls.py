from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('banner-list/', views.list_banner, name='list_banner'),
    path('banner-create/', views.create_banner, name='create_banner'),
    path('banner-detail/<int:id>/', views.banner_detail, name='banner_detail'),
    path('banner-edit/<int:id>/', views.banner_edit, name='banner_edit'),
    path('banner-delete/<int:id>/', views.banner_delete, name='banner_delete'),
    
    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    
    path('aboutus-list/', views.aboutus_list, name='aboutus_list' ),
    path('aboutus-create/', views.create_aboutus, name='create_aboutus'),
    path('aboutus-detail/<int:id>/', views.aboutus_detail, name='aboutus-detail'),
    path('aboutus-edit/<int:id>/', views.aboutus_edit, name='aboutus_edit'),
    path('aboutus-delete/<int:id>/', views.aboutus_delete, name='aboutus_delete'),
    
    path('service-create/', views.create_service, name='create_service'),
    path('service-list/', views.list_service, name='list_service'),
    path('service-detail/<int:id>/', views.service_detail, name='service_detail'),
    path('service-edit/<int:id>/', views.service_edit, name='service_edit'),
    path('service-delete/<int:id>/', views.service_delete, name='service_delete'),
    path('service-delete/', views.service_delete, name='service_delete'),
    
    path('q', views.query, name='query'),


]