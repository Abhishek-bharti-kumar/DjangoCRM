from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    #to check the data is POST or GET and store the data to the field
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        # if user is valid the check and forword to home page
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have login succesfully")
            return redirect('home')
        else:
            messages.success(request, 'Hi... You register yourself')
            return redirect('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    return render(request,'register_user.html',{})