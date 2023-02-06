from django.db import models

# Create your models here.

# customer -- movie -- reservation 

class Movie(models.Model):
    hall = models.CharField(max_length=15)
    movie = models.CharField(max_length=25)
    date = models.DateField()

class Customer(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=15)

class Reservation(models.Model):
    customer = models.ForeignKey('Customer', related_name='reservation', on_delete= models.CASCADE)
    movie = models.ForeignKey('Movie', related_name='reservation', on_delete= models.CASCADE)



