"""semicolon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#end of default code

from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #end of default code

    #a new 'urls' directory has been made in 'blog' app and the 'domain/blog' will be
    # redirected to that directory and then it will be handled
    path('blog/', include('blog.urls')),

    #Now if we want to have landing page (or so) we need to set a path for 
    # empty passed-in string (which means the very first page of the website)
    #I have set it to the 'urls.py' file in 'blog' again because i want my 
    # 'blog' app to be the primary app in the project.
    path('', include('blog.urls')),

]
