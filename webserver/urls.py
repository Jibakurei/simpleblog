"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include,url
from honya.views import *
from honya import views as  honya_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/$',honya_views.api,name='api'),
    url(r'^$',select,name='select'),
    url(r'^add/$', honya_views.add, name='add'), 
    url(r'^edit/(\d+)/$',honya_views.edit,name='edit'),
    url(r'^dels/(\d+)/$',honya_views.dels,name='dels'),
]
