from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator
)

from main.validators import(
    validate_even_number
)

# Create your models here.

class student(models.Model):

    GENDERS = (
        ('f','female'),
        ('m','male'),
        ('u','undisclosed')
    )

    #varchar(100)
    name = models.CharField(max_length=100)
    #integer
    roll_number = models.IntegerField(unique=True)
    #can be null in Db
    #cannot be null in ORM
    address = models.TextField(null=True)
    age = models.IntegerField(null =True, validators=[
        MaxValueValidator(150),
        MinValueValidator(0),
        validate_even_number
    ])
    email = models.CharField(max_length=100,null=True,validators=[EmailValidator("Email address is not valid")])
    #can be null both in Db and ORM
    phone_number=models.CharField(max_length=15,null=True,blank=True)

    gender = models.CharField(max_length=1,choices=GENDERS,null=True)

    def __str__(self):
        return self.name
