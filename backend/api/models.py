from django.db import models

class User(models.Model):

    def __str__(self):
        return self.pk

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


