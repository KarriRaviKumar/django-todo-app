from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Tasks

# Create your views here.
def addtask(request):
    task = request.POST['task']
    Tasks.objects.create(tasks=task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method == 'POST':
        update_task = request.POST['task']
        task.tasks = update_task
        task.save()
        return redirect('home')
    else:
        context = {
            'get_task': task,
        }
        return render(request,'edit_task.html',context)

def delete_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.delete()
    return redirect('home')