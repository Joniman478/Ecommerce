from django.shortcuts import render, get_object_or_404
from .models import *

def store(request, category_slug=None):
    categories = None
    products = None 
    if category_slug is not None:
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        print(1)
    else:
        products = Product.objects.all().filter(is_available=True)
        print(2)
    product_count = products.count()   
    context = {"products":products, "product_count":product_count}
    print(category_slug)
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug=None, product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {"single_product":single_product}
    return render(request, 'store/product_detail.html', context)