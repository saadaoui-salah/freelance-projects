from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.get_orders),
    path('apply', views.apply)
]