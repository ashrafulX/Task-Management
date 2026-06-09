from django.shortcuts import render,redirect
from users.forms import CS_RegisterForm

def sign_up(request):
    
    form=CS_RegisterForm()
    if request.method=='POST':
        form=CS_RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-up')

    return render(request,'register.html',{'form':form})


def sign_in(request):
    pass