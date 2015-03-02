# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20150128_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=9)),
                ('phone', models.CharField(max_length=10)),
                ('state', models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], blank=True, max_length=2, null=True)),
                ('city', models.CharField(null=True, blank=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(null=True, blank=True, max_length=50)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, max_length=2, null=True)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(null=True, blank=True, max_length=75)),
                ('cell_phone', models.CharField(null=True, blank=True, max_length=25)),
                ('work_phone', models.CharField(null=True, blank=True, max_length=25)),
                ('other_phone', models.CharField(null=True, blank=True, max_length=25)),
                ('attended', models.ManyToManyField(null=True, blank=True, to='programs.Session', related_name='attendees')),
                ('household', models.ForeignKey(null=True, related_name='members', blank=True, to='households.Household')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonSubtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personsubtype',
            name='person_type',
            field=models.ForeignKey(to='households.PersonType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='person_subtype',
            field=models.ForeignKey(null=True, blank=True, to='households.PersonSubtype'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.ForeignKey(null=True, blank=True, to='households.PersonType'),
            preserve_default=True,
        ),
    ]
