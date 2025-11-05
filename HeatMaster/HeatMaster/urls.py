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
    path('thermoregulator/', views.thermoregulator, name='thermoregulator'),
    path('aquastrage/', views.aquastrage, name='aquastrage'),
    path('cable/', views.cable, name='cable'),
    path('infrared-cable/', views.infraredCable, name='infrared-cable'),
    path('pruity-of-snowmelt/', views.pruityOfSnowmelt, name='pruity-of-snowmelt'),
    path('thin-laminate-cable/', views.thinLaminateCable, name='thin-laminate-cable'),
    path('thin-cable/', views.thinCable, name='thin-cable'),
    path('thermostats/', views.thermostat_list, name='thermostat_list'),
    path('thermostats/type/<int:type_id>/', views.thermostat_list, name='thermostat_list_by_type'),
    path('thermostat/<int:pk>/', views.thermostat_detail, name='thermostat_detail'),
    path('thermostat/<int:thermostat_id>/comments/create/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    # cart
    path('cart/add/<int:thermostat_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/item/<int:item_id>/update/', views.update_cart_item, name='update_cart_item'),
    path('cart/item/<int:item_id>/remove/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('admin/', admin.site.urls),
    path('videos/', views.videos, name='videos'),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('calculate_price/', views.calculate_price, name='calculate_price'),
    path('heated-mats/', views.heated_mats, name='heated_mats'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery-payment/', views.delivery_payment, name='delivery_payment'),
    path('cooperation/', views.cooperation, name='cooperation'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TODO: path('cart') count products in cart