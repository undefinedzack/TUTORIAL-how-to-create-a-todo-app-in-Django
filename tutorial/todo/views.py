from django.shortcuts import render, redirect

from .models import Tasks
from .forms import AddTaskForm

# Create your views here.
def index(request):

    tasks = Tasks.objects.all()
    form = AddTaskForm()

    context = {
        'tasks' : tasks,
        'form' : form,
    }

    return render(request, 'todo/index.html', context)

def addTask(request):

	form = AddTaskForm(request.POST)

	if form.is_valid():
		form.save()

	return redirect('/')


    