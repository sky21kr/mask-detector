from django.contrib import admin
from . import models

@admin.register(models.MaskHistory)
class MaskHistoyAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'outing',
        'wearing',
        'withMask',
    )