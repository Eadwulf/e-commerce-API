from django.db import models


class Order(models.Model):
    user = models.ForeignKey('accounts.User',
                             on_delete=models.PROTECT,
                             related_name='orders')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"""
            {self.user.username.capitalize()}\'s order | order No. {self.pk}
        """


class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order',
                              on_delete=models.PROTECT,
                              related_name='order_items')
    product = models.ForeignKey('products.Product',
                                on_delete=models.PROTECT,
                                related_name='order_items')

    # product_values ensures that the values of the product
    # at the time of order are stored in the order item.
    product_values = models.JSONField()

    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        # Ensure that a product can only be added once to an order.
        unique_together = ['order', 'product']

    def __str__(self) -> str:
        return f"""
            {self.order.user.username.capitalize()}\'s order item |
            order item No. {self.pk}
        """
