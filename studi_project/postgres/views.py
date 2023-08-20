from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django_dump_die.middleware import dd

from .models import Product, Promotion, Category


def filtered_products(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = None
        
    return products

def get_filtered_products(request, filter=None):
    products = Product.objects.all()

    if filter == 'promotion':
        products = products.filter(promotion__isnull=False)
    elif filter == 'search':
        item_search = request.GET.get('item-search')
        if item_search:
            products = products.filter(label__icontains=item_search)

    return products


def remove_expired_promotions():
    now = timezone.now()
    expired_promotions = Promotion.objects.filter(end_date__lt=now)
    expired_promotions.delete()

def index(request):
    remove_expired_promotions()
    
    active_promotion = Promotion.objects.filter(
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    ).first()
    
    categories = Category.objects.all()

    products = get_filtered_products(request, 'promotion')

    for product in products:
        if active_promotion and product.promotion:
            product.price_promo = product.price - (product.price * (active_promotion.percentage / 100))
            product.save()
        else:
            product.price_promo = None
            product.save()

    return render(request, 'index.html', {"products": products, "categories": categories})

def catalog(request):
    products = get_filtered_products(request)
    return render(request, 'catalog.html', {"products": products})

def promotion(request):
    products = get_filtered_products(request, 'promotion')
    return render(request, 'promotion.html', {"products": products})

def search(request):
    products = get_filtered_products(request, 'search')
    return render(request, 'search.html', {"products": products})

def category(request):
    products = filtered_products(request)
    category = "Il n'ya pas de produits"
    if products:
        category = products[0].category.label
    context = {
        "products": products,
        "category": category
    }
    return render(request, 'category.html', context)
    
    
