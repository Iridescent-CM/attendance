from django.db import models

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

STATE_CHOICES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming'),
)
    
class Household(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class ParentGuardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    cell_phone = models.CharField(max_length=25, null=True, blank=True)
    work_phone = models.CharField(max_length=25, null=True, blank=True)
    other_phone = models.CharField(max_length=25, null=True, blank=True)

    RELATION_CHOICES = (
        ('P', 'Parent'),
        ('S', 'Sibling'),
        ('G', 'Grandparent'),
        ('O', 'Other'),
    )
    relation = models.CharField(max_length=1, choices=RELATION_CHOICES, null=True, blank=True)

    household = models.ForeignKey('Household', null=True, blank=True, related_name='parentguardians')

    class Meta:
        verbose_name = "Parent/Guardian"

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    cell_phone = models.CharField(max_length=10, null=True, blank=True)

    attended = models.ManyToManyField('programs.Session', null=True, blank=True, related_name='attendees')
    household = models.ForeignKey('Household', null=True, blank=True, related_name='students')

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
