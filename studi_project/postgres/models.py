import django_dump_die
from django.db import models

# Create your models here.
# class Teacher(models.Model):
# name = models.CharField(max_length=80)
# age = models.IntegerField()
from django.utils import timezone


class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Promotion(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    percentage = models.IntegerField()

    # product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return f"{self.percentage}% off"


class Product(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, blank=True, null=True, on_delete=models.SET_NULL)
    price_promo = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.label
