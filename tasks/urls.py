from django.urls import path
from tasks.views import dashboard, user_dashboard, manager_dashboard,test,create_task,view_task

urlpatterns = [
    path('dashboard/',dashboard),
    path('user-dashboard/',user_dashboard),
    path('manager-dashboard/',manager_dashboard),
    path('tasks/',test),
    path('create-task/',create_task),
    path('view-task/',view_task),
]
