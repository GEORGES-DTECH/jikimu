
from rest_framework import serializers

from .models import  Mpesa

class MpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpesa
        fields = '__all__' 
       