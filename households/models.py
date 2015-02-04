from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    attended = models.ManyToManyField('programs.Session', null=True, blank=True, related_name='attendees')

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
