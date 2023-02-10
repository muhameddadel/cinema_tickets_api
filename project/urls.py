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
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # first way : json response from django without rest and model
    path('django/jsonresponsenomodel/', views.no_rest_no_model), 
    # second way : json response from django without rest and with model 
    path('django/jsonresponsewithmodel/', views.no_rest_with_model),
    # thrid way 3.1 : GET POST from REST framework -> function based view -> @api_view
    path('rest/fbv_with_rest/', views.fbv_with_rest), 
    path('rest/fbv_with_rest/<int:pk>', views.fbv_pk_with_rest), 
]