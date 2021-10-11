from .models import Account
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms


class UserCreationForm(UserCreationForm):
   
  


   
    
    class Meta:
        model = Account
        fields = [
            'username',
           
            'id_number',
           
            'password1',
            'password2',
             'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'id_number','password1', 'password2','email']:
          
           
            self.fields["email"].help_text= "Required incase of you forget your password."
            self.fields["password1"].help_text= "Enter a simple but unique password."
            self.fields["password2"].help_text= "Enter same password as before."

class UserEditForm(UserChangeForm):
   
   
    
    class Meta:
        model = Account
        fields = [
            'username',
            'id_number',
             'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'id_number','email']:
          
           
            self.fields[fieldname].help_text= None
          