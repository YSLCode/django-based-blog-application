#This file is made to help the re-use of the app in other projects.
#The urls file in the main project directory includes a redirect to this file
#and this file will then handle everything in 'blog' section of the website.

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #The desired view is imported from the views.py file and
    # we will use the 'home' function
    #we name our path as "blog"
    #The first parameter is left empty. Because the 'urls.py' file in the main directory
    # chops off the specified url. so there will be an empty string at the end
    # passed to this file and therefore, we leave the passed-in string empty
    path('', views.home, name='blog-home'),

    #The 'About' page handler
    #To access this page, this time we need to have '/blog/about' in the url
    path('about/', views.about, name='blog-about'),
]