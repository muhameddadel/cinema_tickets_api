from django.shortcuts import render
from django.http import Http404
from django.http.response import JsonResponse
from .models import Customer, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView
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

# third way - with REST framework -> FBV = Function Based Views
# 3.1 GET POST
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
    

# 3.2 GET PUT DELETE
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

# fourth way - with REST framework -> CBV = Class Based View
# 4.1 List and Create == GET and POST 
class CBV_Way(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSeiralizer(customer, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSeiralizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
# 4.2 GET PUT DELETE -> CBV = Class Based View -- pk 
class CBV_Pk(APIView):
    
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk = pk)
        except Customer.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSeiralizer(customer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSeiralizer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# fifth way - with REST framework -> Mixins -> extention of Class Based View
# 5.1 mixins list -> GET POST
class Mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSeiralizer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

# 5.2 mixins get put delete
class Mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSeiralizer

    def get(self, request, pk):
        return self.retrieve(request)
    def post(self, request, pk):
        return self.update(request)
    def delete(self, request, pk):
        return self.destroy(request)

# sixth way -> Generics 
# 6.1 GET and POST
class Generics_list(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSeiralizer


# 6.1 GET , PUT and DELETE
class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSeiralizer