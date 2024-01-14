from django.shortcuts import render
from rest_framework import viewsets

from myapp.models import SubTask, Task
from myapp.serializers import SubTaskSerializer, TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    
    def perform_destroy(self, instance):
        if not instance.is_complete():
            super().perform_destroy(instance)
