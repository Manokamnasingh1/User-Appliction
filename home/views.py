from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    return render(request, 'index.html') 
def login(request):
    return render(request, 'login.html')     




def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
       
        pass1 = request.POST['pass']
       

        # check for errorneous input
        #username should be under 10 characters
        if len(username) > 10:
            messages.error(request,"username must be under 10 characters")
            return redirect('home')
        #username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers")
            return redirect('home')
        #passwords should match
        
        # Create the user
       
        
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials,Please try again")
            return redirect('home')

    return  HttpResponse("404 - Not found")

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')