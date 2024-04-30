from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/approve')
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        email=request.POST.get('Email')
        password=request.POST.get('Password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/')
    return render(request,'signup.html')