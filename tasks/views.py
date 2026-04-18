from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def user_dashboard(request):
    return render(request,'dashboard/user-dashboard.html')

def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

def test(request):
    context ={
        'name':['afsana','ashraful','incoming...'],
        'age':10
    }
    return render(request,'test.html',context)