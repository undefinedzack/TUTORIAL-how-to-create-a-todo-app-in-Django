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

def deleteTask(request, id):

	task = Tasks.objects.get(pk = id)

	task.delete()

	return redirect('/')

def completedTask(request, id):

	task = Tasks.objects.get(pk = id)
	
	task.completed = True
	task.save()

	return redirect('/')

def updateTask(request, id):

	task = Tasks.objects.get(pk = id)
	updateForm = AddTaskForm(instance = task)

	if request.method == 'POST':
		form = AddTaskForm(request.POST, instance = task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'updateForm' : updateForm,
		'key' : id,
		
		'tasks' : Tasks.objects.all(),
	}

	return render(request, 'todo/index.html', context)

def deleteAllCompleted(request):

	completedTasks = Tasks.objects.filter(completed__exact=True).delete()

	return redirect('/')

def deleteAll(request):

	Tasks.objects.all().delete()

	return redirect('/')