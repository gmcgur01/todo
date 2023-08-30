from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.middleware.csrf import get_token
from api.models import Task, User
import json


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
    
    tasks = Task.objects.filter(user=user_id)

    res = json.dumps([{"taskId" : t.pk, "title" : t.title} for t in tasks])
    
    return HttpResponse(res)

def add_task(request, user_id):
    if request.method != "POST":
        return HttpResponseBadRequest("Expected POST request")
    
    user = get_object_or_404(User, pk=user_id)
    
    title = request.POST["title"]
    if title == None:
        return HttpResponseBadRequest("Missing title from request body")

    task = Task(user=user, title=title)
    task.save()
    
    return HttpResponse(task.pk)

def delete_task(request, task_id):
    if request.method != "DELETE":
        return HttpResponseBadRequest("Expected DELETE request")
    
    task = Task.objects.get(pk=task_id)
    task.delete()

    return HttpResponse()

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrfToken" : csrf_token})