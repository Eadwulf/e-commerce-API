# Generated by Django 4.2 on 2023-04-23 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_available'),
        ('carts', '0003_remove_cart_total'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]
