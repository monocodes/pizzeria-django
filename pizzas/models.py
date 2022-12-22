from django.db import models

# Create your models here.

class Topping(models.Model):
    """Pizza toppings that belongs to pizzas."""
    #pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Pizza(models.Model):
    """A pizza the user can choose from."""
    name = models.CharField(max_length=100)
    topping = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name