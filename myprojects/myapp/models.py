from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    team = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myapp_user_groups',
        blank=True,
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myapp_user_permissions',
        blank=True,
        verbose_name='user permissions',
    )

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_complete = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)

class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)