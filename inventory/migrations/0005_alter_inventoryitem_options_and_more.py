# Generated by Django 4.2 on 2023-04-22 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category'),
        ('inventory', '0004_rename_inventory_inventoryitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryitem',
            options={'ordering': ['-added_on'], 'verbose_name': 'Inventory Item', 'verbose_name_plural': 'Inventory Items'},
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inventory', to='products.product', unique=True),
        ),
    ]
