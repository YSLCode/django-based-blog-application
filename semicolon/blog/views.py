from django.shortcuts import render
#end of default code
from django.http import HttpResponse

#views

#function "home". this function is going to handle traffic from the homepage of the blog.
#this function is going to take in request argument. we will return what we want
# the user to see.
def home(request):
    return HttpResponse('<h1>Welcome to SemiColon home</h1>')


#This function will handle the "About" page
def about(request):
    return HttpResponse('About SemiColon')

