from django.contrib import admin
from households import models
from identifiers import models as identifiers

class KeytagInline(admin.TabularInline):
    model = identifiers.Keytag

class StudentWithKeytags(admin.ModelAdmin):
    inlines = [KeytagInline]
    search_fields = ('first_name', 'last_name', 'keytags__barcode', 'zip_code')
    list_display = ('last_name', 'first_name', 'zip_code', '_keytags')
    list_display_links = ('last_name', 'first_name')
    filter_horizontal = ('attended',)

    def _keytags(self, obj):
        return ', '.join(str(x) for x in obj.keytags.all())

admin.site.register(models.Student, StudentWithKeytags)
