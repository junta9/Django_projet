from django.contrib import admin
from .models import Product, Promotion, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('label', 'description', 'price', 'promotion', 'price_promo')


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'percentage')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Promotion, PromotionAdmin)
