from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin
from programs import models
from households import models as households

class SessionInline(admin.TabularInline):
    model = models.Session

class ProgramWithSessions(admin.ModelAdmin):
    inlines = [ SessionInline ]

class AttendeeInline(admin.TabularInline):
    model = households.Student.attended.through

class SessionAdminForm(forms.ModelForm):
    attendees = forms.ModelMultipleChoiceField(
        queryset=households.Student.objects.all(),
        required= False,
        widget=FilteredSelectMultiple(
            verbose_name='Students',
            is_stacked=False
        )
    )

    class Meta:
        model = models.Session

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

    list_display = ('__str__', 'program', 'description', 'time', 'date')

admin.site.register(models.Program, ProgramWithSessions)
admin.site.register(models.Session, SessionAdmin)
