from django.urls import path
from .import views
urlpatterns=[
 path('home',views.home,name='home'),
 path('about',views.about,name='about'),
 path('menu',views.menu,name='menu'),
 path('contact',views.contact,name='contact'),
 path('base',views.base,name='base'),
 
]