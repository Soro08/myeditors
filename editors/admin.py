from django.contrib import admin
from . import models
# Register your models here.

class ValidationHtmlInline(admin.TabularInline):
    model = models.ValidationHtml
    extra = 0


@admin.register(models.Enonce)
class EnonceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description')
    list_display_links = ('titre',)
    inlines = [
        ValidationHtmlInline,
    ]

@admin.register(models.ValidationHtml)
class ValidationHtmlAdmin(admin.ModelAdmin):
    list_display = ('balise', 'attribue', 'attribue_value', 'niveau', 'many', 'nombre')
    list_display_links = ('balise', 'attribue')