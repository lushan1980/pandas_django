from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)