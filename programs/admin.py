from django.contrib import admin
from programs import models

class SessionInline(admin.TabularInline):
    model = models.Session

class ProgramWithSessions(admin.ModelAdmin):
    inlines = [ SessionInline ]

class SessionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'program', 'description', 'time', 'date')

admin.site.register(models.Program, ProgramWithSessions)
admin.site.register(models.Session, SessionAdmin)
