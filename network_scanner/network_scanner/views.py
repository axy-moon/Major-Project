from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth

def login(request):
    if request.method == 'POST':
        username = request.POST['user-name']
        password = request.POST['password']

        user = auth.authenticate(request,username = username,password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Login")
    else:
        return render(request,'main.html')    
def register(request):
    return render(request,'register.html')
