from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin
from programs import models
from households import models as households

class SessionInline(admin.TabularInline):
    model = models.Session

class ProgramWithSessions(admin.ModelAdmin):
    inlines = [ SessionInline ]
    list_display = ('name', 'id', 'session_count')
    search_fields = ('name',)

    def session_count(self, obj):
        return obj.sessions.count()
    session_count.short_description = '# Sessions'

class AttendeeInline(admin.TabularInline):
    model = households.Person.attended.through

class SessionAdminForm(forms.ModelForm):
    attendees = forms.ModelMultipleChoiceField(
        queryset=households.Person.objects.all(),
        required= False,
        widget=FilteredSelectMultiple(
            verbose_name='Attendees',
            is_stacked=False
        )
    )

    class Meta:
        model = models.Session
        exclude = []

    def __init__(self, *args, **kwargs):
        super(SessionAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['attendees'].initial = self.instance.attendees.all()

    def save(self, commit=True):
        session = super(SessionAdminForm, self).save(commit=False)

        if commit:
            session.save()

        if session.pk:
            session.attendees = self.cleaned_data['attendees']
            self.save_m2m()

        return session

class SessionAdmin(admin.ModelAdmin):
    form = SessionAdminForm

    list_display = ('description', 'program', 'time', 'date', 'attendee_count', 'id')
    search_fields = ('description', 'program__name')

    def attendee_count(self, obj):
        return obj.attendees.count()
    attendee_count.short_description = '# Attendees'

admin.site.register(models.Program, ProgramWithSessions)
admin.site.register(models.Session, SessionAdmin)
