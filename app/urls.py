from django.urls import path, include
from . import views

urlpatterns = [    
    path("",views.RegisterPage, name="registerpage"),
    path("register/",views.UserRegister, name="register"),
    path("login/",views.LoginPage, name="loginpage"),
    path("loginuser/",views.UserLogin, name="login"),

]