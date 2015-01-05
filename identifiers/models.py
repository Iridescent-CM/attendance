from django.db import models

class Keytag(models.Model):
    barcode = models.CharField(max_length=20)
    holder = models.ForeignKey('households.Student', related_name='keytags')

    def __str__(self):
        return self.barcode
