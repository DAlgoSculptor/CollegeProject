"""
URL configuration for CollegeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from CollegeApp import views

admin.site.site_header = "Danish Nawaz "
admin.site.site_title = "Danish Admin Portal"
admin.site.index_title = "Welcome to Danish Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('college/' , views.college , name="college"),
    path('', views.home, name='home'),
    path('home/' , views.home , name='home' ),
    path('about/' , views.About ,name='about' ),
    path('services/' , views.services , name='services'),
    path('contact/' , views.contact , name='contact'),
    path('Scan/' , views.Scan , name='contact'),
    path('upload_and_scan_image/', views.upload_and_scan_image, name='upload_and_scan_image'),

]