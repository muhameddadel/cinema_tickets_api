from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=15)
    movie = models.CharField(max_length=25)
   

    def __str__(self) -> str:
        return self.movie

class Customer(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey('Customer', related_name='reservation', on_delete= models.CASCADE)
    movie = models.ForeignKey('Movie', related_name='reservation', on_delete= models.CASCADE)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
    body = models.TextField()

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user = instance)

