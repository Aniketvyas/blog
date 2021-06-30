from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is None:
            messages.info(request,'Invalid Credentials')
            return redirect('/')

        else:
            auth.login(request,user)
            messages.info(request,'Login Success')
            return redirect('/')

def logout(request):
    auth.logout(request)
    messages.info(request,'logout successfull')
    return redirect('/')
            
