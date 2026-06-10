from django.shortcuts import render,redirect
from users.forms import CS_RegisterForm ,RegisterForm
from django.contrib.auth import authenticate,login,logout


def sign_up(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-up')

    return render(request,'register.html',{'form':form})


def sign_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def sing_out(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
