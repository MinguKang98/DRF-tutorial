from django.db.models import fields
from rest_framework import serializers
from . import models


class MovieSerializer(serializers.ModelSerializer):
    # director_name = serializers.RelatedField(source="director", read_only=True)
    # cast = serializers.ReadOnlyField(source="cast.name")
    # get cast name instead of id
    class Meta:
        model = models.Movie
        fields = (
            "id",
            "title",
            "year",
            "cover_image",
            "running_time",
            "director",
            "cast",
        )
