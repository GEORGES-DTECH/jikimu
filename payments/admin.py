
from django.contrib import admin
from .models import Mpesa

class Mpesaadmin(admin.ModelAdmin):
   
    list_display = ('lending_date','full_name','TransID','mpesa_repayment','MSISDN','BusinessShortCode','BillRefNumber')
    search_fields = ()
    list_per_page = 80
    filter_horizontal = ()
    list_filter =()
    fieldsets = ()

admin.site.register(Mpesa,Mpesaadmin)
