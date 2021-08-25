from rest_framework import generics
from . import models
from . import serializers


class CategoryList(generics.ListCreateAPIView):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
