from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from api.models import Task, User


def index(request):
    return HttpResponse("Hello, world!")

def new_user(request):
    if request.method != "GET":
        return HttpResponseBadRequest("Expected GET request")
    
    u = User()
    u.save()
    
    return HttpResponse(u.pk)

def tasks(request, user_id):
    if request.method != "GET":
        return HttpResponseBadRequest("Expected GET request")
    
    tasks = Task.objects.get(user=user_id)
    
    return HttpResponse(", ".join([t.title for t in tasks]))

def add_task(request, user_id):
    if request.method != "POST":
        return HttpResponseBadRequest("Expected POST request")
    
    user = get_object_or_404(User, pk=user_id)
    
    title = request.POST["title"]
    if title == None:
        return HttpResponseBadRequest("Missing title from request body")

    task = Task(user=user, title=title)
    task.save()
    
    return HttpResponse()

# routes that we will want to have:

## get all the tasks for a given user
## create a new task 
## update a task
## delete a task
