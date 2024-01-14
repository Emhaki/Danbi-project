from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team, related_name='tasks')
    content = models.TextField()
    is_complete = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)


class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    teams = models.ManyToManyField(Team, related_name='subtasks')
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)