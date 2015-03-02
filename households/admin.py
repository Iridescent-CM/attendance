from django.contrib import admin
from households import models
from identifiers import models as identifiers

class KeytagInline(admin.TabularInline):
    model = identifiers.Keytag

class PersonWithKeytags(admin.ModelAdmin):
    inlines = [KeytagInline]
    search_fields = ('first_name', 'last_name', 'keytags__barcode', 'household__name')
    list_display = ('last_name', 'first_name', '_keytags', 'household', 'id')
    list_display_links = ('last_name', 'first_name')
    list_filter = ('person_type__name', 'person_subtype__name')
    filter_horizontal = ('attended',)
    fields = (
        'last_name',
        ('first_name', 'middle_name'),
        ('person_type', 'person_subtype'),
        ('sex', 'birthdate'),
        'email',
        ('cell_phone', 'work_phone', 'other_phone'),
        'household',
        'schools',
        'attended'
    )

    def _keytags(self, obj):
        return ', '.join(str(x) for x in obj.keytags.all())

class PersonInline(admin.StackedInline):
    model = models.Person
    extra = 1
    fields = (
        'last_name',
        ('first_name', 'middle_name'),
        ('person_type', 'person_subtype'),
        ('sex', 'birthdate'),
        ('cell_phone', 'work_phone', 'other_phone'),
        'email',
    )

class HouseholdWithMembers(admin.ModelAdmin):
    inlines = [PersonInline]
    fields = ('name', 'address', ('city', 'state', 'zip_code'), 'phone')
    list_display = ('name', 'city', 'zip_code', 'id')
    search_fields = ('name',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'global_id', 'city', 'zip_code', 'id')
    list_filter = ('global_id_type',)
    fields = (
        ('global_id_type', 'global_id_value'),
        'name', 
        'address', 
        ('city', 'state', 'zip_code'), 
        ('phone', 'fax', 'website')
    )
    search_fields = ('name', 'global_id_type', 'global_id_value') 

    def global_id(self, obj):
        return "{}: {}".format(obj.global_id_type, obj.global_id_value)
    global_id.short_description = 'Global ID'

admin.site.register(models.Household, HouseholdWithMembers)
admin.site.register(models.Person, PersonWithKeytags)
admin.site.register(models.PersonType)
admin.site.register(models.PersonSubtype)
admin.site.register(models.School, SchoolAdmin)
