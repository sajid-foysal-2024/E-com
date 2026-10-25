from multiprocessing import context

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from accounts.forms import RegisterForm


# Create your views here.

def register(request):
    form = RegisterForm()
    context={
        'form':form
    }
    return render(request,'accounts/register.html',context)



def login(request):
    return render(request,'accounts/login.html')



def logout(request):
    return render(request,'accounts/logout.html')