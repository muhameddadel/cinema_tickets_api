from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Customer, Movie, Reservation
# Create your views here.

# first way - without REST and no model query FBV
def no_rest_no_model(request):
    customers = [
        {
            'id':1, 
            'name': 'Muhamed', 
            'mobile': 123456789,
        },
        {
            'id': 2,
            'name': 'Adel',
            'mobile': 987654321,
        }
    ]
    return JsonResponse(customers , safe=False)

# second way - without REST and with model query FBV
def no_rest_with_model(request):
    data = Customer.objects.all()
    movie = Movie.objects.all()
    reservation = Reservation.objects.all()
    response = {
        'customers': list(data.values()),
        'movie': list(movie.values()),
        'reservation': list(reservation.values())
    }
    return JsonResponse(response, safe=False)
