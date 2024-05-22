"""
URL configuration for meetcommerce project.

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
from meetcommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("<str:name>",views.greet, name="greet"), # Parameter send kerna k tariqa
    path('',views.homePage,name='home'),  #blank k mutlab hai home page
    path('about-us/',views.about, name='about'),
    path('services/',views.services, name='services'),
    path('projects/',views.projects, name='projects'),
    path('contacts/',views.contacts, name='contacts'),
    path('userform/',views.userForm, name='userform'),
    path('submitform/',views.submitForm, name='submitform'),
    path('calculator/',views.calculator, name='calculator'),
    path('even-odd/',views.evenOdd, name='evenodd'),
    path('marksheet/',views.markSheet),
    path('courses/<int:courseid>',views.courseDetail),   
]
