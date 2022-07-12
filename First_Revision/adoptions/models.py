from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=50, blank=True)
    submission_date = models.DateField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name