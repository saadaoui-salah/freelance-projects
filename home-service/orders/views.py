from django.shortcuts import render

def get_orders(request):
    return render(request, 'orders/orders.html')