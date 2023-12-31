from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')

def Home(request):
    return render (request,'home1.html')  

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('landing')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def Registerpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('landing')
        


    return render (request,'register.html')     

def LogoutPage(request):
    logout(request)
    return redirect('landing')
    
def Dashboard(request):
    return render (request,'dashboard.html')  

def About(request):
    return render (request,'about.html')

def Services(request):
    return render (request,'services.html')

def Insurance(request):
    return render (request,'insurance.html')

def Hostel(request):
    return render (request,'hostel.html')

def Food(request):
    return render (request,'food.html')

def Calculator(request):
    return render (request,'calculator.html')

def Landing(request):
    return render (request,'landing.html')

