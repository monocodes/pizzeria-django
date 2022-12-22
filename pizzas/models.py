from django.db import models

# Create your models here.

class Pizza(models.Model):
    """A pizza the user can choose from."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name