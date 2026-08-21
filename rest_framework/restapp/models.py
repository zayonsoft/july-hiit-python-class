from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
