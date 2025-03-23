"""
URL configuration for HeatMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home.css, name='home.css')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home.css')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thermoregulator/',views.thermoregulator, name='thermoregulator'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('create_blog/',views.create_blog, name='create_blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('admin/', admin.site.urls),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('calculate_price/', views.calculate_price, name='calculate_price'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)