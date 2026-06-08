from django.contrib import admin

# Register your models here.
from tasks.models import Task,TaskDetail,project,employees

admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(project)
admin.site.register(employees)