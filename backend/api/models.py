from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


