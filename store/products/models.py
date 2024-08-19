from enum import unique
from typing import Any, SupportsIndex
from django.db import models

class ProductCategory(models.Model):
	name = models.CharField(max_length=250, unique=True)
	description = models.TextField(unique=True, blank=True)
	
	
	def __str__(self) -> str:
		return self.name
	
class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	description = models.TextField(unique=True, blank=True)
	price = models.DecimalField(max_digits=7, decimal_places=0)
	quantity = models.PositiveIntegerField()
	image = models.ImageField(upload_to="products_images")
	category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)