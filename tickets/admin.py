from django.contrib import admin
from .models import Customer, Movie, Reservation
# Register your models here.

admin.site.register(Customer)
admin.site.register(Movie)
admin.site.register(Reservation)