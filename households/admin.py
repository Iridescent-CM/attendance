from django.contrib import admin
from households import models
from identifiers import models as identifiers

class KeytagInline(admin.TabularInline):
    model = identifiers.Keytag

class StudentWithKeytags(admin.ModelAdmin):
    inlines = [KeytagInline]
    search_fields = ('first_name', 'last_name', 'keytags__barcode')
    list_display = ('last_name', 'first_name', '_keytags')
    list_display_links = ('last_name', 'first_name')
    filter_horizontal = ('attended',)

    def _keytags(self, obj):
        return ', '.join(str(x) for x in obj.keytags.all())

class ParentGuardianInline(admin.StackedInline):
    model = models.ParentGuardian
    extra = 1
    fields = (
        'last_name',
        ('first_name', 'middle_name'),
        ('sex', 'relation'),
        'email',
        ('cell_phone', 'work_phone'),
        'other_phone'
    )

class StudentInline(admin.StackedInline):
    model = models.Student
    extra = 1
    fields = (
        'last_name',
        ('first_name', 'middle_name'),
        ('sex', 'birthdate', 'cell_phone'),
        'email',
    )

class HouseholdWithMembers(admin.ModelAdmin):
    inlines = [ParentGuardianInline, StudentInline]
    fields = ('name', 'address', ('state', 'zip_code'), 'phone')

admin.site.register(models.Student, StudentWithKeytags)
admin.site.register(models.Household, HouseholdWithMembers)
admin.site.register(models.ParentGuardian)
