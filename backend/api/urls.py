from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
    path("<int:user_id>/add-task/", views.add_task, name="add-task"),
    path("<int:user_id>/tasks/", views.tasks, name="tasks")
]