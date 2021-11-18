from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_profile),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
]