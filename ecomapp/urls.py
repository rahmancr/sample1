from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home),
    path('customer_register', views.register),
    path('login', views.login),
    # path('productlist', views.product_view),


]