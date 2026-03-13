from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tasks/', views.get_tasks),
    path('tasks/create/', views.create_task),
    path('tasks/update/<int:pk>/', views.update_task),          #pk is primary key of the task to be updated
    path('tasks/delete/<int:pk>/', views.delete_task),          #pk is primary key of the task to be deleted
] 