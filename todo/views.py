from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    #For testing route
    # return HttpResponse('The form is submitted')

    # Retrieve POST data
    # print(request.POST['task'])
    task = request.POST['task']

    #Create task object
    Task.objects.create(task=task)

    return redirect('home')    
