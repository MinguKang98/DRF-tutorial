from rest_framework import viewsets
from . import serializers
from . import models


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializers
