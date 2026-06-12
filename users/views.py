from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import CS_RegisterForm ,RegisterForm,sign_in_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def sign_up(request):

    form=RegisterForm()

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active=False
            user.save()
            messages.success(request,'A confirmation mail send your email, please activate your account')
            return redirect('sign-in')

    return render(request,'register.html',{'form':form})


def sign_in(request):
    form=sign_in_form()
    if request.method=='POST':
        form=sign_in_form(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def sign_out(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


def activate_user(request,user_id,token):
    try:
        user=User.objects.get(id=user_id)
        if user.is_active:
            return HttpResponse('User Already Activated')
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid Tokens or Id')
    except  Exception as e :
        return HttpResponse(('User Not Found'))
        