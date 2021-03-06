from multiprocessing.dummy import Array
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Borough(models.Model):
    name = models.CharField(max_length=175)
    image = models.CharField(max_length = 220)
    
    def __str__(self):
        return f'{self.name}, NY'

class Neighborhood(models.Model):
    name = models.CharField(max_length=175)
    description = models.TextField(max_length=275)
    image = models.CharField(max_length=250)
    borough = models.ForeignKey(Borough, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.borough.name}'

class Review(models.Model):
    ratings = models.IntegerField(
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ])
    description = models.TextField(max_length = 300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point_of_interest_id = models.CharField(max_length=220, null=True)

    def __str__(self):
       return f'{self.point_of_interest_id} has {self.ratings} rating'


class Itinerary(models.Model):
    points_of_interest = ArrayField(models.CharField(max_length=220, default=list), default=list, blank=True)
    points_of_interest_name = ArrayField(models.CharField(max_length=220), default=list, blank=True)
    points_of_interest_id = ArrayField(models.CharField(max_length=220), default=list, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models. CharField(max_length=100)
    
