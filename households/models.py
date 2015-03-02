from django.db import models
from . import choices

class Household(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=2, choices=choices.STATE_CHOICES, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} [id: {}]".format(self.name, self.id)

class PersonType(models.Model):
    name = models.CharField(max_length=25, verbose_name='Type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type'

class PersonSubtype(models.Model):
    name = models.CharField(max_length=100, verbose_name='Subtype')
    person_type = models.ForeignKey('PersonType')

    def __str__(self):
        return "{}: {}".format(self.person_type.name, self.name)

    class Meta:
        verbose_name = 'Subtype'

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=2, choices=choices.SEX_CHOICES, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    cell_phone = models.CharField(max_length=25, null=True, blank=True)
    work_phone = models.CharField(max_length=25, null=True, blank=True)
    other_phone = models.CharField(max_length=25, null=True, blank=True)

    household = models.ForeignKey('Household', null=True, blank=True, related_name='members')
    person_type = models.ForeignKey('PersonType', null=True, blank=True)
    person_subtype = models.ForeignKey('PersonSubtype', null=True, blank=True)

    attended = models.ManyToManyField('programs.Session', null=True, blank=True, related_name='attendees')

    def __str__(self):
        keytags = ",".join(tag.barcode for tag in self.keytags.all())
        return "{}, {} [id: {}, keytags:{}]".format(self.last_name, self.first_name, self.id, keytags)

    class Meta:
        verbose_name_plural = "People"
