from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskModelForm,TaskDetailModelForm
from tasks.models import Task,TaskDetail
from django.db.models import Q,Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
# Create your views here.

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

def is_manager(user):
    return user.groups.filter(name='Manager').exists()


@login_required
def dashboard(request):
    task=Task.objects.all()
    total_task=task.count()
    completed_task=task.filter(status='COMPLETED').count()
    progress_task=task.filter(status='IN_PROGRESS').count()
    pending_task=task.filter(status='PENDING').count()
    context={
        'total_task':total_task,
        'completed_task':completed_task,
        'progress_task':progress_task,
        'pending_task':pending_task
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required
@user_passes_test(is_employee,login_url='no-permission')
def user_dashboard(request):
    return render(request,'dashboard/user-dashboard.html')


@login_required
@user_passes_test(is_manager,login_url='no-permission')
def manager_dashboard(request):

    dekhi=request.GET.get('dekhi','all')

    # print(dekhi)
    base=Task.objects.prefetch_related('assign_to').select_related('taskdetail')

    if dekhi=='COMPLETED':
        task=base.filter(status='COMPLETED')
    elif dekhi=='IN_PROGRESS':
        task=base.filter(status='IN_PROGRESS')
    elif dekhi=='PENDING':
        task=base.filter(status='PENDING')
    elif dekhi=='all':
        task=base.all()

    
    # total_task=task.count()
    # completed_task=task.filter(status='COMPLETED').count()
    # progress_task=task.filter(status='IN_PROGRESS').count()
    # pending_task=task.filter(status='PENDING').count()


    counts=Task.objects.aggregate(
        total_task=Count('id'),
        completed_task=Count('id',Q(status='COMPLETED')),
        progress_task=Count('id',Q(status="IN_PROGRESS")),
        pending_task=Count('id',Q(status='PENDING'))

    )
    context={
        'task':task,
        'counts':counts
    }
    return render(request, 'dashboard/manager-dashboard.html',context)



@login_required
@permission_required('tasks.add_task',login_url='no-permission')
def create_task(request):
    # emp=employees.objects.all()
    task_form=TaskModelForm()
    task_detail=TaskDetailModelForm()

    # Django form  (eta amra use korbo na)
    if request.method == 'POST':
        task_form=TaskModelForm(request.POST)
        task_detail=TaskDetailModelForm(request.POST)
        print(task_form.errors)
        print(task_detail.errors)
        if task_form.is_valid() and task_detail.is_valid():
            '''For Model Form'''

            task=task_form.save()
            detail=task_detail.save(commit=False)
            detail.task=task
            detail.save()

            messages.success(request,'Task Created Succesfully')
            return redirect('create-task')
        
        
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
            

    context={'task_form':task_form,'task_detail':task_detail}
    return render(request,'task_form.html',context)



@login_required
@permission_required('tasks.cange_task',login_url='no-permission')
def update_task(request,id):
    up_id = Task.objects.get(id=id)

    task_detail_obj = TaskDetail.objects.get(task=up_id)

    task_form = TaskModelForm(instance=up_id)
    task_detail = TaskDetailModelForm(instance=task_detail_obj)

    if request.method == 'POST':

        task_form = TaskModelForm(request.POST, instance=up_id)

        task_detail = TaskDetailModelForm(
            request.POST,
            instance=task_detail_obj
        )

        print(task_form.errors)
        print(task_detail.errors)

        if task_form.is_valid() and task_detail.is_valid():

            task = task_form.save()

            detail = task_detail.save(commit=False)
            detail.task = task
            detail.save()

            messages.success(request,'Task updated Successfully')

            return redirect('update-task', up_id.id)

    context = {
        'task_form': task_form,
        'task_detail': task_detail
    }

    return render(request,'task_form.html',context)



@login_required
@permission_required('tasks.delete_task',login_url='no-permission')
def delete_task(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        messages.success(request,'Task Deleted Succesfull')
        return redirect('manager-dashboard')
    else:
        messages.error(request,'something wrong')
        return redirect('manager-dashboard')




@login_required
@permission_required('tasks.view_task',login_url='no-permission')
def view_task(request):
    
    """Select Related Query (foreignkey, one to one)"""
    """Prefetch Related (reverse foreighneky, many to many)"""

    task=Task.objects.select_related('taskdetail').all()
    return render(request,'view_task.html',{'task':task})


@login_required
@permission_required('tasks.view_task',login_url='no-permission')
def task_details(request,id):
    task=Task.objects.get(id=id)
    return render(request,'task_detail.html',{'task':task})