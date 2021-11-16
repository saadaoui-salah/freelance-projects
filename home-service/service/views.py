from django.shortcuts import render
from .models import Review, Service

def get_services(request, category):
    services =  Service.objects.filter(category_id=category)
    context = {'services': services}
    return render(request, 'services/services.html', context=context)

def get_service_detail(request, service_id):
    service =  Service.objects.filter(id=service_id)
    reviews =  Review.objects.filter(service__id=service_id)
    context = {'services': service, 'reviews': reviews}
    return render(request, 'services/services_details.html', context=context)
