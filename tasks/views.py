from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tasks.models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        if title and description:
            task = Task(
                user=request.user, 
                title=title,
                description=description
                )
            task.save()
            
            return redirect("main-page")
        else:
            return redirect("error-page")  
    
    tasks = Task.objects.filter(user=request.user)

    context = {
        'tasks': tasks  
    }
    
    return render(request, 'index.html', context)


def error(request):
    return render(request, 'error.html')


