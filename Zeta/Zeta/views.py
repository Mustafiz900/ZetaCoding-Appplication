from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Trainer.models import Trainer_Signup

# Create your views here.
def index(request):
    return render(request,'index.html')

def AdminLogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pass1=request.POST['passwd']
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"Admin Login Successfull")
            return redirect('/Admin')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/AdLogin')
    return render(request,'AdLogin.html')

def AdminLogout(request):
    logout(request)
    messages.info(request," Admin Logout succesful")
    return redirect('/')


def TrainerSignup(request):
    if request.method=='POST':
        username=request.POST['Uname'] 
        name=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        phone=request.POST['phone']
        if pass1 != pass2:
            messages.error(request,"Password Doest not match")
            return redirect('/TrSignup')
        try:
            if Trainer_Signup.objects.get(username=username):
                messages.error(request,"Username already Exist")
                return redirect('/TrSignup')
        except Exception as identifier:
            pass
        newTrainer=Trainer_Signup(name=name,username=username,email=email,password=pass1,phone=phone)
        newTrainer.save()
        messages.warning(request,"Signup Successfull")
        return redirect('/TrLogin')
        
    return render(request,'TrLogin.html')


def TrainerLogin(request):
    if request.method=='POST':
        uname=request.POST['Username']
        pass1=request.POST['Password']
        try:
            user=Trainer_Signup.objects.get(username=uname,password=pass1)
            if user is not None:
                # login(request,user)
                messages.info(request,"Trainer Login Successfull")
                return redirect('/Trainer/Tdashboard')
        except:
            messages.error(request,"Invalid Credentials")
            return redirect('/TrLogin')
    return render(request,'TrLogin.html')

def TrainerLogout(request):
    logout(request)
    messages.info(request," Trainer Logout succesful")
    return redirect('/')