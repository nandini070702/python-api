from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response           #used to send back a response to the client in json format
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Todo API")       #home page      


@api_view(['GET'])             #decorator to specify that this view should only accept GET requests
def get_tasks(request):
    tasks = Task.objects.all()               #fetch all task objects from the database
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])                        #only accept POST requests
def create_task(request):                              #create a new task object using the data sent in the request body
    serializer = TaskSerializer(data=request.data)         #Takes incoming JSON data from the request.

    if serializer.is_valid():
        serializer.save()                              #save in db
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['PUT'])             #only accept PUT requests
def update_task(request, pk):        #Fetch the task object with the given primary key (pk) from the database and update it with the data sent in the request body.
    task = Task.objects.get(id=pk)          #Fetches the task with that ID from the database.

    serializer = TaskSerializer(task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['DELETE'])            #only accept DELETE requests
def delete_task(request, pk):
    task = Task.objects.get(id=pk)              #Fetches the task with that ID from the database.
    task.delete()

    return Response({"message": "Task deleted"})
