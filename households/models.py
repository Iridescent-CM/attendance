from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    attended = models.ManyToManyField('programs.Session', related_name='attendees')

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
