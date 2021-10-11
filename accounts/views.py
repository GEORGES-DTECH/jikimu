from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from.forms import UserCreationForm,UserEditForm
from django.views import generic

class PasswordsChangeView(PasswordChangeView):
    success_url = reverse_lazy('success_message')
    from_class = PasswordChangeForm

def succesmessage(request):
    return render(request,'accounts/success.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Account created,you can login')
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy ('loans')

    def get_object(self):
        return self.request.user
