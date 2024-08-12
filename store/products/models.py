from enum import unique
from django.db import models

class ProductCategory(models.Model):
	name = models.CharField(max_length=250, unique=True)
	description = models.TextField(unique=True, blank=True)
	
	
class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	description = models.TextField(unique=True, blank=True)
	price = models.DecimalField(max_digits=9999, decimal_places=9)
	quantity = models.PositiveIntegerField()
	image = models.ImageField(upload_to="products_images")
	category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)