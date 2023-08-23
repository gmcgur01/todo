from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

# routes that we will want to have:

## get all the tasks for a given user
## create a new task 
## update a task
## delete a task
