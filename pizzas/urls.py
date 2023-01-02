"""Define URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizzas.
    path('pizza_types/', views.pizza_types, name='pizza_types'),
    # Detail page for a single pizza.
    path('pizza_types/<int:pizza_type_id>/', views.pizza_type, name='pizza_type'),
]