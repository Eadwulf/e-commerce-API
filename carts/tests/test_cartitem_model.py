from django.test import TestCase

from carts.models import CartItem
from carts.tests.helpers import create_cart_item


class SetUp(TestCase):

    def setUp(self):
        self.cart_item = create_cart_item()


class TestCartItem(SetUp):

    def test_cart_item(self):
        self.assertEqual(
            CartItem.objects.filter(pk=self.cart_item.pk).exists(),
            True,
        )
        self.assertEqual(
            CartItem.objects.get(pk=self.cart_item.pk).cart,
            self.cart_item.cart,
        )
        self.assertEqual(
            CartItem.objects.get(pk=self.cart_item.pk).product,
            self.cart_item.product,
        )
        self.assertEqual(
            CartItem.objects.get(pk=self.cart_item.pk).quantity,
            self.cart_item.quantity,
        )
        self.assertEqual(
            CartItem.objects.get(pk=self.cart_item.pk).added_on,
            self.cart_item.added_on,
        )
        self.assertEqual(
            CartItem.objects.get(pk=self.cart_item.pk).updated_on,
            self.cart_item.updated_on,
        )

