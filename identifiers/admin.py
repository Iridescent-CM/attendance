from django.contrib import admin
from identifiers import models

class KeytagAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'holder')

admin.site.register(models.Keytag, KeytagAdmin)
