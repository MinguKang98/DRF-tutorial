from django.contrib import admin
from . import models


@admin.register(models.Movie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "running_time", "director")
