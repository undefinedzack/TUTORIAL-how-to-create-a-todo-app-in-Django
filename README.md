

### Why should we make a To-Do?

- To-Do is super helpful for beginners.
- Any Django project needs a **database** and for that you must know how to handle databases in Django, making a To-Do app makes us learn basic database operations like CRUD i.e. Create, Read, Update and Delete.
- It's fun!

### Requirements
- Just latest version of [python](https://www.python.org/) and we are good to go.


## I. Virtual Environment
---
**[Virtual Environment](https://docs.python.org/3/tutorial/venv.html)** is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

### Creating Virtual Environment

```python
python3 -m venv env
```

![Untitled.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608113285634/6Ae3CeEXl.png)


### Activating Virtual Environment

After creating an Virtual Environment we need to activate it, in order to get inside that virtual space.

```python
source env/bin/activate
```

![Untitled 1.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608113422090/fjLM10hcn.png)


## II. Setting Up Django

---

### Installing Django

Now that we have our **Virtual Environment** set up, lets install Django in it.

```python
pip install django
```


![Untitled 2.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608113511714/5-XEXbxkX.png)

### Creating Django Project

Here we'll have to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

```python
django-admin startproject <Project's Name>
```


![Untitled 3.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608113545828/2HT7cIoxI.png)

This will create a directory named <Project's Name> in your current directory. We'll cd into it. There you'll find two things namely 

- manage.py
- tutorial directory named after your project's name, this directory contains all initial settings for an instance of Django.


![Untitled 4.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608113559028/ctmsM-uSg.png)

## III. Creating our First App

---

Now that we have our initial Django setup ready, we'll create our to-do app.  Each application you write in Django consists of a python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

```python
python3 manage.py startapp <App's Name>
```


![Untitled 5.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608113572234/9zATYA1F_.png)

You'll find a new directory named <App's Name>.  This directory contains all initial settings for our app.

## IV. Integrating our todo app with the project

---

Django uses **plug and play** feature.

What's that?

- Suppose you're working on a large app with plenty of code, a single app won't do much of a help rather than creating confusion and taking eternity to find and fix any issue.
- In this scenario we might create multiple apps for specific features or requirements, this'll make it easy to understand and quick to fix any issue, like if something goes wrong or we just don't want that feature anymore, just pull the plug and everything else still works like a charm.

Following this we need to tell Django which app we want to integrate/plug in. 

- Head to <Project's Name> directory. Open urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),    #add this line
]
```

We'll create todo's [urls.py](http://urls.py) in a moment.

- Head to <Project's Name> directory. Open settings.py. We'll add our todo app into installed apps.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'todo.apps.TodoConfig',    #add this line
]
```

Voila! it's integrated.

## V. Creating Models

---

### [What are Models?](https://docs.djangoproject.com/en/3.1/topics/db/models/#:~:text=A%20model%20is%20the%20single,to%20a%20single%20database%20table.&text=With%20all%20of%20this%2C%20Django,access%20API%3B%20see%20Making%20queries.)

A model is the single, definitive source of information about your data. It contains the essential fields and behaviours of the data you’re storing. Generally, each model maps to a single database table.

Now we need to store data (tasks in our case) somewhere in our To-Do app.  For that we'll create a model named **Tasks**.

- Head to the todo directory, there you'll find '**models.py**'

```python
from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BoolenField(default=False)

		def __str__(self):
        return f"{self.task}"
```

- **task** is a character field (a string) with a max length of 100 i.e. task's can't exceed beyond 100 characters.
- **completed** is a boolean field we'll use to determine whether a particular task is complete or not. By default we'll set it to false i.e. incomplete task.
- **What is __ *str* __ function**?
    1. It's a **string** which model class will return for each individual **Tasks** object. 
    2. For example let's say we have a number of tasks in our database, if we were to identify which task is what, by default Django will return Tasks objects as TasksObject#1, TasksObject#2, TasksObject#3....... now that's not readable, how will we know what TasksObject#3 is? 
    3. Here comes __ *str* __ to our help, we tell Django to return 'task' which is a string in our **Tasks** model, instead of TasksObject#whatever, now we know which task is what.

## VI. Creating URL's

---

### **What are URL's?**

- URL's are the pathways where user can navigate to, like we have written every possible route a end user or an admin can take in our app.
- Now where this pathway lead us to? Here comes view's. Think of view as a destination URL's lead to.
- Django maintains **urlpatterns**, a list where we write our pathway's to our destination's. Let's create

    ```python
    from django.urls import path

    from . import views

    app_name = 'ToDo'
    urlpatterns = [
        path('', views.index, name="Home"),
        path('/addTask', views.addTask, name="Add Task"),
        path('/deleteTask/<int:id>', views.deleteTask, name="Delete Task"),
        path('/completedTask/<int:id>', views.completedTask, name="Task Completed"),
        path('/updateTask/<int:id>', views.updateTask, name="Update Task"),
        path('/deleteAllCompleted', views.deleteAllCompleted, name="Delete all Completed"),
    	path('/deleteAll', views.deleteAll, name="Delete All"),
    ]
    ```

- Each URL is accompanied with a complementary view like **views.<view name>**, our destination.

### Our app has 7 different URL's :

1. Where will user be as soon as he/she opens our app? Well empty URL (' ') i.e. **root** is the answer and we are mapping that empty URL (' ' ) to the index view.
2. **Add Task URL** → this URL adds task in our app's database.
3. **Delete Task URL** → this URL delete's task from our app's database, but question comes which task should be deleted? here comes concept of an unique id, each task has it's own unique id **(primary key)** which Django generates automatically during task creation and maintains it, which needs to be passed in the URL, to identify a particular task.
4. **Completed Task URL** →this URL mark's a task as completed, i.e. changes that default false value we gave to **completed** to true.
5. **Update Task** → this URL is used to Update a task.
6. **Delete All Completed** → this URL is used to remove all the completed tasks from the database, no clutter or mess.
7. **Delete All →** this URL is used to delete all tasks from the database. A reset.

It's time to know what actually happens when we reach our destination using URL's. Let's code views for our URL's.

## VI. Creating Views

---

### **What are Views?**

- Now every time we visit a URL, we make a request asking Django is this destination available? if available, take us to that destination and perform the deeds, else classic 404 NOT FOUND error.
- Views are callable functions which takes in the request, performs the deeds and gets us a response.

Let's create some views

### Index view
---


    from django.shortcuts import render, redirect

    from .models import Tasks
    from .forms import AddTaskForm

    def index(request):

        tasks = Tasks.objects.all()
        form = AddTaskForm()

        context = {
            'tasks' : tasks,
            'form' : form,
        }

        return render(request, 'todo/index.html', context)
  

Everything we write inside any view are our deeds to be performed.

- *tasks = Tasks.objects.all()* → Tasks.objects.all() returns all the task objects in our **Tasks model** in form of a list.
- *form = AddTaskForm()* → We'll get to form's in a bit. For now, we're just initializing an empty AddTaskForm().
- context{} → imagine context as a container, which will carry **contents we mention** from our database to the templates(.html files), so we carry **tasks** and a **form** from our database to the **index.html**.
- *return render(request, 'todo/index.html', context)* → this combines our .html file with the context and renders a response, i.e. **a html page with dynamic content from the database**.

Here we can see our data went from our database to the .html part, where we'll be able to display the data dynamically as per our requirements. What if we wanna do it the reverse way, i.e. we want to send data from the user to the database? FORM'S!

Creating a form → we'll create a new file named [forms.py](http://forms.py) in our todo app

```python
from django import forms
from django.forms import ModelForm

from .models import Tasks

class AddTaskForm(forms.ModelForm):

	task = forms.CharField(max_length = 250,
							widget = forms.TextInput(
								attrs = {
									'class' : 'form-control',
									'placeholder' : 'task?', 
								}
							)
						)

	class Meta:
		model = Tasks
		fields = '__all__'
```

- Here we used a model form, now model forms are forms specific to the models we create in Django, it'll contain all input fields mapped closely to the fields in our model .  To know more about Model form → **[HERE](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/).**
- **task** is a string of max length 250.
- For the text field (task) to look cool we are applying a bootstrap class 'form-control' with placeholder 'task?' as attributes to the widget.


### Add Task view

---

```python
def addTask(request):

	form = AddTaskForm(request.POST)

	if form.is_valid():
		form.save()

	return redirect('/')
```

- *form = AddTaskForm(request.POST)* → We initialize the AddTaskForm but this time with some contents which were passed in with the POST request.
- *if form.is_valid():* →We check whether the form is valid or not.
- *form.save()* → save it to the database.
- *return redirect('/')* → return to the index page.

### Delete Task View
---

```python
def deleteTask(request, id):

	task = Tasks.objects.get(pk = id)

	task.delete()

	return redirect('/')
```

- We get an id of the task to be deleted, with the request.
- *task = Tasks.objects.get(pk = id) →* we get that particular task, with primary key = **id** from the database.
- *task.delete()* → we simply delete that task.

### Completed Task View
---

```
def completedTask(request, id):

	task = Tasks.objects.get(pk = id)
	
	task.completed = True
	task.save()

	return redirect('/')
```

- We get an id of the task to be marked as completed, with the request.
- *task = Tasks.objects.get(pk = id) →* we get that particular task, with primary key = **id** from the database.
- *task.completed = True →* setting the default false value of **completed** to true.
- *task.save() →* save's the task to the database.

### Update Task View
---

```python
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
```

- This one is somewhat tricky, here we get an id of the task to be updated, with the request.
- *task = Tasks.objects.get(pk = id) →* we get that particular task, with primary key = **id** from the database.
- Now that we have to update a task, we need to firstly know **what's in it,** secondly **what changes were made,** and then save it.
- *updateForm = AddTaskForm(instance = task) →*  We created a **AddTaskForm** named **updateForm** with task to be updated as an instance, the '***firstly'*** done.
- *if request.method == 'POST': →* This section combines changes i.e. edits to the task, which were sent via POST request, with the task instance.
    1. *form = AddTaskForm([request.POST](http://request.POST), instance = task) →* We combine our task instance obtained in ***firstly*** part, with the changes made by the user ( request.POST ) into a AddTaskForm.
    2. *if form.is_valid(): →* Check whether the form is valid or not.
    3. *form.save() →* If valid save the form.
    4. *return redirect('/') →* Return to the index page.
- context → Our context has three item: updateForm, key and tasks.
    1. updateForm → Our AddTaskForm with the instance of task to be updated.
    2. key → Id ( primary key ) of the task to be updated.
    3. tasks → List of all tasks in our database.

###  Delete All Completed View
---

```python
def deleteAllCompleted(request):

	completedTasks = Tasks.objects.filter(completed__exact=True).delete()

	return redirect('/')
```

- *completedTasks = Tasks.objects.filter(completed__exact=True).delete() →* We filter out the completed tasks in our database and delete them.

### Delete All View
---

```python
def deleteAll(request):

	Tasks.objects.all().delete()

	return redirect('/')
```

- *Tasks.objects.all().delete() →* We delete all the tasks in our database.

## VII. Creating Templates

---

Here we'll create the **index.html** which we used in our views. It is the end point of our app, like this is what everyone will see and interact with.

- Here we are going to use :
    1. Html
    2. [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - For styling the page
    3. [Font Awesome Icons](https://fontawesome.com/)

```html
<!DOCTYPE html>
<html>

    <head>
        <title>To-Do App</title>
        
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

        <!-- Font Awesome -->
        <script src="https://kit.fontawesome.com/4764f4dcde.js" crossorigin="anonymous"></script>
    </head>

    <body>

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">To-Do</a>
            
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                  <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                  </li>
                </ul>
            </div>
        </nav>
        
        <div class="container mt-4">
            <div class="row">
                <div class="col-12">
                    <div class="card border-info mb-3" >
                        <div class="card-header text-center">My To-Do</div>
                            <div class="card-body text-info">
                                
                                {% if updateForm %}
                                    <form action="{% url 'ToDo:Update Task' key %}" method="post">
                                        {% csrf_token %}
                                        <div class="input-group mb-3 shadow bg-white">
                                            {{ updateForm.task }}
                                            <div class="input-group-append">
                                                <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Add Task</button>
                                            </div>
                                        </div>
                                    </form>
                                
                                {% else %}
                                    <form action="{% url 'ToDo:Add Task' %}" method="post">
                                        {% csrf_token %}
                                        <div class="input-group mb-3 shadow bg-white">
                                            {{ form.task }}
                                            <div class="input-group-append">
                                                <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Add Task</button>
                                            </div>
                                        </div>
                                    </form>
                                {% endif %}

                                <div class="row mt-4">
                                    <div class="col-8">
                                        <h3 class="card-title">Tasks</h3>
                                    </div>
                                    <div class="col-2">
                                        <a href="{% url 'ToDo:Delete all Completed' %}">
                                            <button type="button" class="btn btn-sm btn-outline-info rounded-pill">Remove Completed</button>
                                        </a>
                                    </div>
                                    <div class="col-2 mr-auto">
                                        <a href="{% url 'ToDo:Delete All' %}">
                                            <button type="button" class="btn btn-sm btn-outline-info rounded-pill">Remove All</button>
                                        </a>
                                    </div>
                                </div>
                                
                                

                                {% for task in tasks %}
                                <div class="card mt-2 shadow-sm">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-10">
                                                <a href="{% url 'ToDo:Task Completed' task.id %}">
                                                    {% if task.completed %}
                                                        <del><h5 class="card-title">{{ task }}</h5></del>
                                                    {% else %}
                                                        <h5 class="card-title">{{ task }}</h5>
                                                    {% endif %}
                                                    
                                                    
                                                </a>
                                            </div>
                                            <div class="col-1 close">
                                                <a href="{% url 'ToDo:Update Task' task.id %}">
                                                    <i class="fas fa-marker"></i>
                                                </a>
                                            </div>
                                            <div class="col-1">
                                                <a href="{% url 'ToDo:Delete Task' task.id %}">
                                                    <button type="button" class="close" aria-label="Close">
                                                      <span aria-hidden="true">&times;</span>
                                                    </button>
                                                </a>
                                            </div>    
                                            
                                        </div>                                                                                                            
                                      {% if task.completed %}
                                      <p class="card-text"><small class="text-muted">It's Done!</small></p>
                                      {% endif %}
                                    </div>
                                  </div>
                                {% endfor %}  
                            </div>
                        </div>
                    </div> 
                </div>
            </div>     
        </div>

        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    </body>
</html>
```

- Our header part contains component scripts and links, which we obtain from their respective websites.
    1. [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    2. [Font Awesome Icons](https://fontawesome.com/)
- Now if you have basic bootstrap knowledge, you'll understand the structure of the page.

### Let's get a overview of what's going on

---

- In the upper part of the body, for user to enter task's we have form's with conditions, whether the user is adding a new task or updating a existing task. If updating it'll get us an updateForm with 'task to be updated' instance else AddTaskForm.

    ```html
    {% if updateForm %}
        <form action="{% url 'ToDo:Update Task' key %}" method="post">
            {% csrf_token %}
            <div class="input-group mb-3 shadow bg-white">
                {{ updateForm.task }}
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Add Task</button>
                </div>
            </div>
        </form>

    {% else %}
        <form action="{% url 'ToDo:Add Task' %}" method="post">
            {% csrf_token %}
            <div class="input-group mb-3 shadow bg-white">
                {{ form.task }}
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Add Task</button>
                </div>
            </div>
        </form>
    {% endif %}
    ```

- We are adding two buttons for **delete completed tasks** and **delete all tasks**.

```html
<div class="row mt-4">
    <div class="col-8">
        <h3 class="card-title">Tasks</h3>
    </div>
    <div class="col-2">
        <a href="{% url 'ToDo:Delete all Completed' %}">
            <button type="button" class="btn btn-sm btn-outline-info rounded-pill">Remove Completed</button>
        </a>
    </div>
    <div class="col-2 mr-auto">
        <a href="{% url 'ToDo:Delete All' %}">
            <button type="button" class="btn btn-sm btn-outline-info rounded-pill">Remove All</button>
        </a>
    </div>
</div>
```


- In the final part we'll display all the tasks present in our database with their complete statuses, i.e. we'll strike the completed tasks and display **Done!** We'll also provide the user with update and delete buttons on each task, through which he/she can update or delete any particular task.

```html
		
{% for task in tasks %}
	<div class="card mt-2 shadow-sm">
	    <div class="card-body">
	        <div class="row">
	            <div class="col-10">
	                <a href="{% url 'ToDo:Task Completed' task.id %}">
	                    {% if task.completed %}
	                        <del><h5 class="card-title">{{ task }}</h5></del>
	                    {% else %}
	                        <h5 class="card-title">{{ task }}</h5>
	                    {% endif %}
	                    
	                  
	                </a>
	            </div>
	            <div class="col-1 close">
	                <a href="{% url 'ToDo:Update Task' task.id %}">
	                    <i class="fas fa-marker"></i>
	                </a>
	            </div>
	            <div class="col-1">
	                <a href="{% url 'ToDo:Delete Task' task.id %}">
	                    <button type="button" class="close" aria-label="Close">
	                      <span aria-hidden="true">&times;</span>
	                    </button>
	                </a>
	            </div>    
	            
	        </div>                                                                                                            
	      {% if task.completed %}
	      <p class="card-text"><small class="text-muted">It's Done!</small></p>
	      {% endif %}
	    </div>
	  </div>
	{% endfor %}  
```

## The Result

---


![Untitled 6.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608114188671/BIeukkbP0.png)


![Untitled 7.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1608114198326/tOU3-U6XR.png)

## Resource's

---

1. [Django](https://docs.djangoproject.com/en/3.1/)'s documentation.
2. [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)'s documentation.

Source Code : [HERE](https://github.com/undefinedzack/TUTORIAL-how-to-create-a-todo-app-in-Django)

that's all peeps.......thank you for reading!
