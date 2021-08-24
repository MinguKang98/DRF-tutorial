from django.db import models
from core import models as core_models


class Person(core_models.TimeStampedModel):

    ACTOR = "actor"
    DIRECTOR = "director"
    KIND_CHOICES = ((ACTOR, "Actor"), (DIRECTOR, "Director"))

    name = models.CharField(max_length=120)
    photo = models.ImageField(blank=True)
    kind = models.CharField(max_length=15, choices=KIND_CHOICES)

    def __str__(self):
        return self.name
