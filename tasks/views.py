from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import employees,Task
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


def create_task(request):
    # emp=employees.objects.all()
    form=TaskModelForm()

    # Django form  (eta amra use korbo na)
    if request.method == 'POST':
        form=TaskModelForm(request.POST)
        if form.is_valid():
            '''For Model Form'''
            form.save()
            return render(request,'task_form.html',{'form':form,'message':'Task Added Succesfull'})
        
        
            """FOR DJANGO FORM"""
            # data=form.cleaned_data
            # print(data)
            # title=data.get('task_title')
            # description=data.get('description')
            # due_date=data.get('due_date')
            # assigned_to=data.get('assigned_to')

            # task=Task.objects.create(title=title,description=description,due_date=due_date)
            # # Assing emp to task
            # for id in assigned_to:
            #     task.assign_to.add(id)
            

    context={'form':form}
    return render(request,'task_form.html',context)


def view_task(request):
    task=Task.objects.all()
    return render(request,'view_task.html',{'task':task})