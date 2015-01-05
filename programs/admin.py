from django.contrib import admin
from programs import models
from households import models as households

class SessionInline(admin.TabularInline):
    model = models.Session

class ProgramWithSessions(admin.ModelAdmin):
    inlines = [ SessionInline ]

class AttendeeInline(admin.TabularInline):
    model = households.Student.attended.through

class SessionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'program', 'description', 'time', 'date')
    inlines = [ AttendeeInline ]

admin.site.register(models.Program, ProgramWithSessions)
admin.site.register(models.Session, SessionAdmin)
