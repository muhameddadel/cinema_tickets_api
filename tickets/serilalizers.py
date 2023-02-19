from rest_framework import serializers
from .models import Customer, Movie, Reservation, Post


class MovieSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class CustomerSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['pk','reservation', 'name', 'mobile']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"