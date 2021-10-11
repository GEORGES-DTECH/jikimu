from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class Mymanager(BaseUserManager):
    def create_user(self,id_number,username,email,password=None):
        if not email:
            raise ValueError("users must have an email")
        
       
        
        
        if not username:
            raise ValueError("enter username")
        
        if not id_number:
            raise ValueError("enter id")
       
        user = self.model(
              email = self.normalize_email(email),
              id_number=id_number,
      
              username = username,
             
             

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,id_number,email,password=None):
         
        user = self.create_user(
              email = self.normalize_email(email),
              
              username=username,
            
            
              password = password,
              id_number=id_number
        ) 
        user.is_admin = True
      
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
       


class Account(AbstractBaseUser):
   
    email = models.EmailField(verbose_name="email",max_length=60,blank=True,unique=True)
    username = models.CharField(max_length=30,unique=True)
    id_number = models.CharField(max_length=30,unique=True,default="")
    last_login = models.DateTimeField(verbose_name="last_login",auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date_joined",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
  
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = "id_number"
    REQUIRED_FIELDS = [
        'email',
       
        'username'
       
    
        
        ]
    objects = Mymanager()

    def __str__(self):
        return self.username 

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_lable):
        return True    


   

 