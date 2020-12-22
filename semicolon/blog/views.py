from django.shortcuts import render
from .models import Post
# end of default code
# Code: from django.http import HttpResponse
# The import above is used when we need to return pure html code instead of template.

# views


# function "home". this function is going to handle traffic from the homepage of the blog.
# this function is going to take in request argument. we will return what we want
# the user to see.
def home(request):

    # In order to pass out posts' data to the template we create 'context'
    context = {
        'posts': Post.objects.all()
    }

    # return HttpResponse('<h1>Welcome to SemiColon home</h1>')
    # the code above is used for html code but it will be a mess
    # to write a whole file with it. so we use templates in templates
    # folder and use render() in django.shortcuts module to return them.
    # the render() function already returns an HttpResponse in the background
    return render(request, 'blog/home.html', context)
    # the 'blog' directory here is actually the one in the 'templates' directory
    # Adding 'context' as the third parameter, will allow us to use our data in
    # pur templates


# This function will handle the "About" page
def about(request):
    # return HttpResponse('About SemiColon')
    # The same as the home function happens here
    return render(request, 'blog/about.html', {'title': 'About'})
    # The third parameter passed, has to be a dictionary and the
    # keys and values will be passed to the template
