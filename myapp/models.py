from django.contrib.auth.models import AbstractUser
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class CustomUser(AbstractUser):
    # Add custom fields if needed
    pass
