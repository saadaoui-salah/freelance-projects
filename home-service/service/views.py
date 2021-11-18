from django.shortcuts import render
from .models import Category, Review, Service

def get_sub_cat(request, category_id):
    sub_cat =  Category.objects.filter(parent_category__id=category_id)
    context = {'sub_cat': sub_cat}
    return render(request, 'service/sub-categories.html', context=context)

def get_services(request, category_id):
    services =  Service.objects.filter(category__id=category_id)
    context = {'services': services}
    return render(request, 'service/services.html', context=context)

def get_categories(request):
    categories =  Category.objects.filter(parent_category=None)
    context = {'categories': categories}
    return render(request, 'home.html', context=context)

def get_service_detail(request, service_id):
    service =  Service.objects.filter(id=service_id)
    reviews =  Review.objects.filter(service__id=service_id)
    context = {'services': service, 'reviews': reviews}
    return render(request, 'services/services_details.html', context=context)
