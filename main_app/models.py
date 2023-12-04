from django.db import models
from django.conf import settings

class User(models.Model):
    username = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="@.com")
    password = models.CharField(max_length=20, default="/")


    def __str__(self):
        return self.username

class Drill_data(models.Model):
    username = models.CharField(max_length=20)
    drill_name = models.CharField(max_length=20)
    amount_completed = models.IntegerField(max_length=20)


class Stats(models.Model):
    userStats = models.ForeignKey(User, on_delete=models.CASCADE)
    drillsComplete = models.IntegerField(default=0)


    def __int__(self):
        return self.drillsComplete

class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def is_author(self, user):
        return self.author == user
