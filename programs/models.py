from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Session(models.Model):
    program = models.ForeignKey('Program', related_name='sessions')
    description = models.CharField(max_length=255)
    time = models.TimeField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{}: {}".format(self.program, self.description)
