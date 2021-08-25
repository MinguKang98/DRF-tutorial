from django.contrib import admin
from . import models


@admin.register(models.Person)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "kind")
