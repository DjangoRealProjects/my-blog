"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
#from blog import views as blog_views ### Add this if you are adding this path: path('', blog_views.home, name='blog-home'),

urlpatterns = [
    path('admin/', admin.site.urls), # keep
    path('', include('blog.urls')), # use this if you want to get to the Home page of our Project=Root URLs
    path('blog/', include('blog.urls')), # corey, it will send whatever matches ? blog to blog.urls. it will chop up the parts that already match and only send the remaining strings
    #path('blog.urls', app_name = ""),
]

