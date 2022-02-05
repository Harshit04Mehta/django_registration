from email import message
from django.shortcuts import render
from .models import *

# Create your views here.
#view for registering page
def RegisterPage(request):
    return render(request,"app/register.html")


# view for user registraion
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST.get('fname', False)
        lname = request.POST.get('lname', False)
        email = request.POST.get('email', False)
        contact = request.POST.get('contact', False)
        password = request.POST.get('password', False)
        cpassword = request.POST.get('cpassword', False)

        #first we will check that user already exists
        user = User.objects.filter(Email=email) 
        if user:
            message = "User already exists"
            return render(request,"app/register.html", {'msg':message})
        else:
            if password==cpassword:
                newuser = User.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact, Password=password) 

                message="User Successfully Registered"
                return render(request,"app/login.html", {'msg':message})
            else:
                message="Password and Confirm Password doesn't match"
                return render(request,"app/register.html", {'msg':message})



#view for login page
def LoginPage(request):
    return render(request,"app/login.html")

#login User
def UserLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        #Checking the emailid with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password ==  password:
                #getting user data in session
                request.session['Firstname'] = user.Firstname 
                request.session['Lastname'] = user.Lastname 
                request.session['Contact'] = user.Contact 
                request.session['Email'] = user.Email
                return render(request, "app/home.html")

            else:
                message= "Password Doesn't match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message="User Doesn't Exist"
            return render(request,"app/register.html",{'msg':message})