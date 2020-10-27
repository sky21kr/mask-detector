from django.contrib import admin
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'source',
        'date',
    )

@admin.register(models.MaskHistory)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'outing',
        'wearing',
    )