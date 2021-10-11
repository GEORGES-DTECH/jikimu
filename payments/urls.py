from django.urls import path

from . import views
from .views import (
    
    C2BConfirmationAPIView,
    C2BValidationAPIView
  

)

urlpatterns = [

     
     path('validation/',
         C2BValidationAPIView.as_view(), name='validation'),
     
     path('confirmation/',
         C2BConfirmationAPIView.as_view(), name='confirmation'),      




]
