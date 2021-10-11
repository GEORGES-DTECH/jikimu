import sys
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.functional import cached_property
from django.db.models import Sum
from decimal import Decimal
from django.db.models import FloatField
from django.db.models.functions import Cast
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
import calendar
from io import BytesIO
from PIL import Image, ImageOps
from django.core.files import File
import uuid
from django.core.files.uploadedfile import InMemoryUploadedFile


class Mpesa(models.Model):
    LOAN_PERIOD= (
        ('1month', '1month'),
        ('2months', '2months'),
      
       
    )

    APPROVAL= (
        ('approved', 'approved'),
        ('waiting approval', 'waiting approval'),
        ('cleared', 'cleared'),
        ('pending', 'pending'),
        ('not approved', 'not approved'),
     )
    
    INTEREST= (
        (Decimal('0.20'), '0.20'),
       
    )
    
    TransID = models.CharField(max_length=20,blank=True,null=True)
    TransTime = models.CharField(max_length=50,null=True,blank=True)
    TransAmount = models.CharField(max_length=200,null=True,blank=True)
    interest_charged = models.DecimalField(decimal_places=3,max_digits=3 ,choices=INTEREST,default=Decimal("0.20"))
    mpesa_repayment = models.DecimalField(decimal_places=2,max_digits=9,blank=True,null=True)
    loan_amount = models.IntegerField(blank=True,null=True)
    cash_repayment = models.IntegerField(default=0)
    MSISDN= models.CharField(max_length=15,blank=True,null=True)
    full_name = models.CharField(max_length=50,blank=True,null=True)
    FirstName = models.CharField(max_length=50,blank=True,null=True)
    LastName = models.CharField(max_length=50,blank=True,null=True)
    BusinessShortCode = models.CharField(max_length=50,blank=True,null=True)
    BillRefNumber = models.CharField(max_length=50,blank=True,null=True)
    lender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name="Payments")
    loan_period = models.CharField(choices=LOAN_PERIOD, max_length=100,blank=True,default="1month")
    status = models.CharField(choices=APPROVAL, max_length=100,blank=True,default="waiting approval")
    lending_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse ('mpesa')

    
    
    @cached_property
    def get_mpesa_repayment(self):
        amount = float(self.TransAmount)
        return amount
    
    @cached_property
    def get_full_name(self):
        method1 = self.FirstName.lower()
        method2 = self.LastName.lower()
        client_name = f'{method1} {method2}'
        return client_name

    def save(self, *args, **kwargs):
        self.full_name = self.get_full_name
        self.mpesa_repayment = self.get_mpesa_repayment  
        super(Mpesa, self).save(*args, **kwargs)  

   










































''' 
{
   "TransactionType":"Pay Bill",
   "TransID":"RKTQDM7W6S",
   "TransTime":"20191122063845",
   "TransAmount":"10",
   "BusinessShortCode":"600638",
   "BillRefNumber":"254708374149",
   "InvoiceNumber":"",
   "OrgAccountBalance":"49197.00",
   "ThirdPartyTransID":"",
   "MSISDN":"254708374149",
   "FirstName":"John",
   "MiddleName":"",
   "LastName":"Doe"
}



'''
