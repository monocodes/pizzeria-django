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

def pizza_type(request, pizza_type_id):
    """Show a single pizza type and all its toppings."""
    pizza_type = Pizza.objects.get(id=pizza_type_id)
    toppings = pizza_type.topping.all()
    context = {'pizza_type': pizza_type, 'toppings': toppings}
    return render(request, 'pizzas/pizza_type.html', context)