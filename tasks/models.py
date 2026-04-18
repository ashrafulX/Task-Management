from django.db import models
 
class employees(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

# Create your models here.
class Task(models.Model):
    project=models.ForeignKey("project",on_delete=models.CASCADE,default=1)
    assign_to=models.ManyToManyField(employees)

    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.DateField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 


class TaskDetail(models.Model):
    assigned_to=models.CharField(max_length=100)
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


class project(models.Model):
    project_name=models.CharField(max_length=100)
    start_date=models.DateField()

