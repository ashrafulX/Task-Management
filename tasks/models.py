from django.db import models
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail


class employees(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

# Create your models here.
class Task(models.Model):
    status_choices=[
        ('PENDING','pending'),
        ('IN_PROGRESS','in progress'),
        ('COMPLETED','completed'),
    ]
    project=models.ForeignKey("project",on_delete=models.CASCADE,default=1)
    assign_to=models.ManyToManyField(employees)

    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=15,choices=status_choices,default='PENDING')
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title

class TaskDetail(models.Model):
    # assigned_to=models.CharField(max_length=100)
    HIGH="H"
    MEDIUM='M'
    LOW='L'
    priority_options=(
        (HIGH,'High'),
        (MEDIUM, 'Medium'),
        (LOW,'Low')
    )
    priority=models.CharField(max_length=1,choices=priority_options,default=LOW)
    task=models.OneToOneField(Task,on_delete=models.CASCADE)
    notes=models.TextField(blank=True,null=True)
    def __str__(self):
        return f"Details from Task {self.task.title}"


class project(models.Model):
    project_name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    start_date=models.DateField()

    def __str__(self):
        return self.project_name
    
@receiver(m2m_changed,sender=Task.assign_to.through)
def notify_email_task_create(sender,instance,action,**kwargs):
    if action=='post_add':
        mail=[emp.email for emp in instance.assign_to.all()]
        send_mail(
        "Task Assigned",
        f"A task Has been Assigned {instance.title}.",
        "ashraf452b@gmail.com",
        mail,
        )


# 1. Show the tasks which are assigned to a specific employee --

# 2. Show all employees working on a specific project

 # 3. Get all tasks that are due today --

# 4. Show all tasks with a priority higher than 'low'

# 5. Get the number of tasks completed by a specific employee

# 6. Get the most recently assigned task  -- next time try

# 7. Show all projects that have no tasks assigned

# 8. Show tasks that have been overdue for more than a week

# 9. Get the total count of tasks assigned to each employee

# 10. Get tasks that are either 'completed' or 'in-progress'