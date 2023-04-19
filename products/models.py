from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    specifications = models.JSONField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey('accounts.User',
                               on_delete=models.PROTECT,
                               related_name='products')

    class Meta:
        unique_together = ['vendor', 'name']

    def __str__(self) -> str:
        return self.name