from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/admin/programs/program/%i" % self.id

    def __str__(self):
        return "{} [id: {}]".format(self.name, self.id)

class Session(models.Model):
    program = models.ForeignKey('Program', related_name='sessions')
    description = models.CharField(max_length=255)
    time = models.TimeField(null=True, blank=True)
    date = models.DateField()

    def get_absolute_url(self):
        return "/admin/programs/session/%i" % self.id

    def __str__(self):
        return "{}: {}".format(self.program, self.description)
