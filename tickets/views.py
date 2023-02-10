from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Customer, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from .serilalizers import CustomerSeiralizer, MovieSeiralizer, ReservationSeiralizer
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

# third way - with REST framework -> Function Based Views
# 3.1 GET POSt
@api_view(['GET', 'POST'])
def fbv_with_rest(request):
    
    # GET 
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSeiralizer(customers, many = True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = CustomerSeiralizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    

# 3.1 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def fbv_pk_with_rest(request, pk):
    try:
        customer = Customer.objects.get(pk = pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET 
    if request.method == 'GET':
        serializer = CustomerSeiralizer(customer)
        return Response(serializer.data)
    
    # PUT
    elif request.method == 'PUT':
        serializer = CustomerSeiralizer(customer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
