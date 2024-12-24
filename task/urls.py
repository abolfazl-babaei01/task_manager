from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.home, name='home'),
    path('task-details/<int:task_id>/', views.task_details, name='task-details'),
    path('create_task/', views.create_task, name='create_task'),
]