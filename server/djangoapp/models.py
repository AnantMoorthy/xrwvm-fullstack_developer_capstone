# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
# - Name
    name = models.CharField(max_length=100)
# - Description
    description = models.TextField()
# - Any other fields you would like to include in car make model
    VIN = models.CharField(max_length=17)
# - __str__ method to print a car make object
    def __str__(self):
        return self.name # Return the name as the string representation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Name
    name = models.CharField(max_length=100)
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('RACE', 'Race'), 
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
# - Year (IntegerField) with min value 2015 and max value 2023
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
    def __str__(self):
        return self.name  # Return the name as the string representation
