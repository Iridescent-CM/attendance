from django.contrib import admin
from identifiers import models

class KeytagAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'holder')
    fields = ['barcode', 'holder', 'holder_link']
    readonly_fields = ['holder_link']

    def holder_link(self, obj):
        return '<a href="%s">%s</a>' % (obj.holder.get_absolute_url(), obj.holder)
    holder_link.allow_tags = True

admin.site.register(models.Keytag, KeytagAdmin)
