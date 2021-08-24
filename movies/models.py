from django.db import models
from core import models as core_models


class Movie(core_models.TimeStampedModel):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    cover_image = models.ImageField(blank=True)
    # rating
    # category
    running_time = models.IntegerField()
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person")

    def __str__(self):
        return self.title
