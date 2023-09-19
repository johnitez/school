from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('home.html',views.home,name='home' ),
    path('about.html',views.about,name='about' ),
    path('testimonials.html',views.testimonials,name='testimonials' ),
    path('contact.html',views.contact,name='contact' ),
    path('apply.html',views.apply,name='apply' ),
]