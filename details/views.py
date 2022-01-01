from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from .form import registration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
# Create your views here.


# This Fuction Will Add new Item and show All Items
@login_required(login_url='login')
def add_show(request):
    if request.method == 'POST':
        fm = registration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = registration()
            messages.success(request, 'Your details has been submited')
    else:
        fm = registration()
    infor = User.objects.all()
    return render(request, 'add.html', {'form':fm, 
    'inf':infor})

#this function will update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk= id)
        fm = registration(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
            messages.success(request, 'Your details has been updated please Click the Back To Home')

    else:
        pi = User.objects.get(pk= id)
        fm = registration(instance=pi)
    return render(request, 'update.html', {'form':fm})






#This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)  
        pi.delete()
        messages.success(request, 'Your details has been successfully deleted..!')
        return HttpResponseRedirect('/')



def register(request):
    if request.user.is_authenticated:
        return redirect('addshow')
    else:

        if request.method == 'POST':
            fm = registration(request.POST)
            if fm.is_valid():
                fname = fm.cleaned_data.get('name')
                lname = fm.cleaned_data.get('lastname')
                fm.save()
                fm = registration()
                messages.success(request, 'Form has been successfully submited for ' + fname +" " + lname)
                return redirect('login')
            else:
                messages.info(request, "Something went wrong Please try again OR Please check your Password and Confirm Password!")
            
            
        fm = registration()
        return render(request, 'register.html', {'form':fm})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('addshow')
    else:
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('addshow')

            else:
                messages.info(request, 'username OR password is incorrect')

            
        context = {}
        return render(request, 'login.html', context)
        

def logoutpage(request):
    logout(request)
    return redirect('login')