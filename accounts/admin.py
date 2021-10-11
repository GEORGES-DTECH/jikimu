from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account

class Accountadmin(UserAdmin):
    list_display = ('is_staff','date_joined','id_number','username','last_login')
    search_fields = ('id_number',)
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()

admin.site.register(Account,Accountadmin) 