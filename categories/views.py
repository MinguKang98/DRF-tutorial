from rest_framework import mixins
from rest_framework import generics
from . import models
from . import serializers


class CategoryList(
    generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin
):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
