from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def index(request):
    products = Product.objects.filter(available=True)
    return render(request, 'main/index/index.html', {'products': products})

def popular_list(request):
    product = Product.objects.filter(available = True)[:3]
    return render(request,
                  'main/index/index.html',
                  {'products': product})

def product_detail(request, slug):
    from main.models import Product 
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'main/product/detail.html', {'product': product})