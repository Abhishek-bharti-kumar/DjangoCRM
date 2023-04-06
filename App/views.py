from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SingUpForm
from .models import Record

def home(request):
    #Fetch Record from database
    records = Record.objects.all()
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
        return render(request,'home.html',{"records":records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password,)
            login(request, user)
            messages.success(request,'you have succesfully registered')
            return redirect('home')
    else:
        form = SingUpForm()    
        return render(request,'register_user.html',{'form':form})
    
    return render(request,'register_user.html',{'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        coust = Record.objects.get(id=pk)
        c_record = {"coust":coust}
        return render(request,'record.html',c_record)
    else:
        messages.success(request,'goto home page')
        return redirect('home')