from django.shortcuts import render
from products.models import Product, ProductCategory

def index(request):
    context = {
        "title": "Store Main Page",
        "sale": "Аутлет: до -70% Собственный бренд. -20% новым покупателям.",
        "is_sale": True,
    }
    
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        "title": "Store-Catalog",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }
    
    return render(request, 'products/products.html', context)