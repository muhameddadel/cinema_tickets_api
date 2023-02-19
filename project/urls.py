"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('customers', views.Viewsets_customer)
router.register('movies', views.Viewsets_movie)
router.register('reservation', views.Viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # first way : json response from django without rest and model
    path('django/jsonresponsenomodel/', views.no_rest_no_model), 

    # second way : json response from django without rest and with model 
    path('django/jsonresponsewithmodel/', views.no_rest_with_model),

    # thrid way 3.1 : GET POST from REST framework -> function based view -> @api_view
    path('rest/fbv_with_rest/', views.fbv_with_rest), 

    # thrid way 3.2 : GET, PUT and DELETE from REST framework -> function based view -> @api_view
    path('rest/fbv_with_rest/<int:pk>', views.fbv_pk_with_rest), 

    # fourth way 4.1 : GET and POST from REST framewok -> class based view -> class CBV(APIview)
    path('rest/cbv/', views.CBV_Way.as_view()), 
    
    # fourth way 4.2 : GET, PUT and DELETE from REST framewok -> class based view -> class CBV(APIview)
    path('rest/cbv/<int:pk>', views.CBV_Pk.as_view()), 
    
    # fifth way 5.1 : GET, POST from REST framewok(CBV)
    # Mixins -> class Mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView)
    path('rest/mixins/', views.Mixins_list.as_view()), 
    
    # fifth way 5.2 : GET, PUT and DELETE from REST framewok(CBV)
    # Mixins -> class Mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView)
    path('rest/mixins/<int:pk>', views.Mixins_pk.as_view()), 

    # sixth way 6.1 : GET, POST from REST framewok(CBV) -> Generics
    path('rest/generics/', views.Generics_list.as_view()), 

    # sixth way 6.2 : GET, PUT and DELETE from REST framewok(CBV) -> Generics
    path('rest/generics/<int:pk>', views.Generics_pk.as_view()), 
    
    # seventh way 7.1 : GET, POST from REST framewok(CBV) -> Viewsets
    path('rest/viewsets/', include(router.urls)), 

    # eighth way -> find movie with function based view
    path('fbv/findmovie', views.find_movie),

    # ninth way -> create reservation with function based view
    path('fbv/createreservation', views.create_reservation),

    # rest auth url 
    path('api-auth', include('rest_framework.urls')),

    # Token authentication
    path('token-auth', obtain_auth_token),

    # post pk generics permissions
    path('post/generic/<int:pk>', views.Post_pk.as_view())
]