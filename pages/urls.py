from django.urls import path
from . import views

urlpatterns = [
   path('temp', views.temp, name='temp'),
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   #path('admin/', views.admin_page, name='admin_page')
   ]
