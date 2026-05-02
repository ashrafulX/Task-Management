from django.db import models
 
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
    notes=models.TextField(blank=True,null=True)
    def __str__(self):
        return f"Details from Task {self.task.title}"


class project(models.Model):
    project_name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    start_date=models.DateField()

    def __str__(self):
        return self.project_name

