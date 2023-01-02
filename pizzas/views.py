from django.shortcuts import render

from .models import Pizza

# Create your views here.

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizza_types(request):
    """Show all pizzas."""
    pizza_types = Pizza.objects.order_by('name')
    context = {'pizza_types': pizza_types}
    return render(request, 'pizzas/pizza_types.html', context)