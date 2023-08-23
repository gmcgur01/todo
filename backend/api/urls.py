from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new-user/", views.new_user, name="new-user"),
    path("<int:user_id>/add-task/", views.add_task, name="add-task"),
    path("<int:user_id>/tasks/", views.tasks, name="tasks")
]