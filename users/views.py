from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import  RegisterForm,sign_in_form,AssignRoleForm,CreateGroupForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from django.views import View

    
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

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

    return render(request,'dashboard/register.html',{'form':form})


def sign_in(request):
    form=sign_in_form()
    if request.method=='POST':
        form=sign_in_form(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    return render(request,'dashboard/login.html')

@login_required
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
        
@user_passes_test(is_admin,login_url='no-permission')
def admin_dashboard(request):
    users=User.objects.all()
    return render(request,'admin/dashboard.html',{'users':users})


@user_passes_test(is_admin,login_url='no-permission')
def assign_role(request,user_id):
    form=AssignRoleForm()
    user=User.objects.get(id=user_id)
    if request.method=='POST':
        form=AssignRoleForm(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request,'User {user.username} has been assigned {role.name} role')
            return redirect('admin-dashboard')
    
    return render(request,'admin/assign_role.html',{'form':form})

@user_passes_test(is_admin,login_url='no-permission')
def create_group(request):
    form=CreateGroupForm()
    if request.method=='POST':
        form=CreateGroupForm(request.POST)
        if form.is_valid():
            group=form.save()
            messages.success(request,f'{group} Has been created succesfully!')
            return redirect('creat-group')
    return render(request,'admin/create_group.html',{'form':form})

@user_passes_test(is_admin,login_url='no-permission')
def group_list(request):
    groups=Group.objects.all()
    return render(request,'admin/group_list.html',{'groups':groups})