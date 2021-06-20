from django.db import models


# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('F', 'Female'), ('M', 'Male')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=40)
    breed = models.CharField(max_length=40, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    # The vaccination class attribute is ManyToManyField relationship
    # because one dog is compatible with many vaccines and vice versa.
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name