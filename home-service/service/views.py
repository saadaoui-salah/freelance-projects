from django.shortcuts import render


def get_services(request, category):
    return render(request, 'services/services.html')


def apply(request):
    return render(request, 'services/apply.html')