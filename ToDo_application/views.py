from django.shortcuts import render
from todo.models import Tasks

def home(request):
    task_not_completed = Tasks.objects.filter(is_completed=False).order_by('-modified_at')
    task_completed = Tasks.objects.filter(is_completed=True).order_by('-modified_at')
    context = {
        'n' : task_not_completed,
        'c' : task_completed
    }
    return render(request,'home.html',context)
