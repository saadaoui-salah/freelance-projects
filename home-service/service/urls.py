from django.urls import path
from . import views

urlpatterns = [
    path('category=<int:category_id>', views.get_sub_cat, name="sub_cat"),
    path('sub-cat=<int:category_id>', views.get_services, name="services"),
    path('', views.get_categories, name="categories"),
    path('service=<int:service_id>', views.get_categories, name="details"),
]