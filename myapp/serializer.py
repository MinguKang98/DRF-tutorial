from django.db.models import fields
from . import models
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=models.Person
        fields=('first_name','last_name')
