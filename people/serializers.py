from django.db.models import fields
from rest_framework import serializers
from . import models


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = (
            "id",
            "name",
            "photo",
            "kind",
        )
