from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Address
from .forms import CustomUserCreationForm, ProfileForm, AddressForm
from django.contrib import messages

def loginUser(request):
    page="login"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User name does not exist!!")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
           messages.error(request, "User name and password are incorrect!!!")
    return render(request, 'login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "Successfully logout")
    return redirect('login')

def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account is created successfully!!!")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,"Error Occured During registration !!")
    context = {'page':page,'form':form}
    return render(request,"login_register.html",context)

@login_required(login_url='login')
def index(request):
    return render(request,'welcome.html')

@login_required(login_url='login')
def profile(request):
    #
    obj = Profile.objects.all()
   
    return render(request,'profiles.html',context={'obj':obj})