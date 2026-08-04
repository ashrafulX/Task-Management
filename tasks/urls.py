from django.urls import path
from tasks.views import dashboard, user_dashboard, manager_dashboard,create_task,view_task,update_task,delete_task,task_details

urlpatterns = [
    path('dashboard/',dashboard),
    path('user-dashboard/',user_dashboard),
    path('manager-dashboard/',manager_dashboard , name='manager-dashboard'),
    path('create-task/',create_task,name='create-task'),
    path('view-task/',view_task),
    path('tasks/<int:id>/details/',task_details,name='task-details'),
    path('update-task/<int:id>/',update_task,name='update-task'),
    path('delete-task/<int:id>/',delete_task,name='delete-task'),
]
