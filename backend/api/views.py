from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from api.models import Task, User


def index(request):
    return HttpResponse("Hello, world!")

def users(request):
    if request.method != "GET":
        return HttpResponseBadRequest()
    
    users = User.objects.all()

    return HttpResponse(", ".join([str({"id" : u.pk, "user_name" : u.user_name}) for u in users]))

def tasks(request, user_id):
    if request.method != "GET":
        return HttpResponseBadRequest()
    
    tasks = Task.objects.get(user=user_id)
    
    return HttpResponse(", ".join([t.title for t in tasks]))

def add_task(request, user_id):
    if request.method != "POST":
        return HttpResponseBadRequest()
    
    print(request.body)

    task = Task(user=user_id, title=request.body["title"])
    task.save()
    
    return HttpResponse()

# routes that we will want to have:

## get all the tasks for a given user
## create a new task 
## update a task
## delete a task
