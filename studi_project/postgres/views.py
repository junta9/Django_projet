from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django_dump_die.middleware import dd

from .models import Product, Promotion


def index(request):
    products = Product.objects.all()

    active_promotion = Promotion.objects.filter(
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    ).first()

    if active_promotion:
        for product in products:
            if product.promotion:
                product.price_promo = product.price - (product.price * (active_promotion.percentage / 100))
                product.save()
    else:
        for product in products:
            product.price_promo = None
            product.save()

    return render(request, 'index.html', {"products": products})
