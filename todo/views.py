from django.shortcuts import render, redirect, get_object_or_404
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

def markAsDone(request, pk):    
   
    task = get_object_or_404(Task, pk=pk)
    
    urlPathList = request.path.split('/')

    # IF path contains mark-as-done
    isCompleted = "mark-as-done" in urlPathList
    
    task.is_completed = isCompleted
    task.save()

    return redirect('home')
    # return HttpResponse('ok')

def editTask(request, pk):

    get_task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        new_task = request.POST['task']

        get_task.task = new_task
        get_task.save()    

        return redirect('home')
    else:
        context = {
            'get_task' : get_task 
        }

        return render(request, 'edit_task.html', context)
