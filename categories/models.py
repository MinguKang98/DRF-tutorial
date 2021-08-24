from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
