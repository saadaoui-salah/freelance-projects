from django.urls import path
from . import views

urlpatterns = [
    path('<str:category>', views.get_services),
    path('apply', views.apply)
]