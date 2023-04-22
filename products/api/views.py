from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework import status
from rest_framework.response import Response

from products.models import Product
from products.api.serializers import ProductSerializer

from inventory.models import InventoryItem


class ProductListView(ListCreateAPIView):
    model = Product
    queryset = model.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            InventoryItem.objects.create(
                product=product,
                quantity=request.data.get('quantity', 1),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductSingleView(RetrieveUpdateDestroyAPIView):
    model = Product
    queryset = model.objects.all()
    serializer_class = ProductSerializer

