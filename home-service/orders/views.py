from django.http.response import Http404
from django.shortcuts import render
from .models import Order


def get_orders(request):
    orders = Order.objects.filter(user__id=request.user.id)
    context = {'orders': orders}
    return render(request, 'orders/orders.html', context=context)


def apply(request):
    if request.method == 'POST' and request.user.is_athenticated() :
        obj = Order.objects.create(user=request.user, service=request.POST['service'], description=request.POST['description'])
        obj.save()
        return render(request, 'services/apply.html', context={'message': 'order created'})
    return render(request, 'services/apply.html', context={'message': 'order not created'})
    