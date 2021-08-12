from rest_framework import viewsets
from . import serializer
from . import models

class PersonViewSet(viewsets.ModelViewSet):
    queryset=models.Person.objects.all()
    serializer_class=serializer.PersonSerializer
