# Generated by Django 4.2.4 on 2023-08-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgres', '0006_remove_promotion_product_product_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_promo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
