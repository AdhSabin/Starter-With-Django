from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signuppage(request):
    error_message = None

    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass1']

        if pass1 != pass2:
            error_message = "Your password and confirm password do not match!" 
        elif User.objects.filter(username=uname).exists():
            error_message = "Username already exists!"
        elif User.objects.filter(email=email).exists():
            error_message = "Email already in use!" 
        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save() 
            return redirect('login')  

    return render(request, 'signup.html', {'error_message': error_message}) 

def loginpage(request):
    error_message = None
    
    if request.method == "POST":
        uname = request.POST['name']
        pass1 = request.POST['pass']
        user = authenticate(request,username=uname,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('library')

        else: 
             error_message = "Username or password is incorrect!!!"
        
    return render(request,'login.html',{'error_message': error_message})  


@login_required(login_url='login')
def home(request):
    return render (request,'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('login') 