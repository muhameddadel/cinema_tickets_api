from django.contrib import admin
from .models import Customer, Movie, Reservation, Post
# Register your models here.

admin.site.register(Customer)
admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Post)